# Privacy Preservation Techniques

We cover 3 types of such approaches, namely (1)MPC (2) HE and (3)DP

## Secure Multi-party computation

Secure Multi-Party Computation a.k.a secure function evaluation, was initially introduced as a secure two-party computation problem.

MPC allows us to compute functions of private input value so that each party learns only the corresponding function output value, but not input values from other parties. For example, given a secret value $x$ that is split into $n$ shares so that a party $P_i$ only knows $x_i$ all party can collaborative compute

$$ y_1,...,y_n = f(x_1,...x_n)$$

so the party $P_i$ learns nothing beyond the output value $y_i$ corresponding to its own input $x_i$

The standard approach to prove that MPC protocol is secure is the ***simulation paradigm.*** To prove an MPC protocol is secure against adversaries that corrupt $t$ parties under the simulation paradigm, we build a simulator that, when given inputs and outputs of $t$ colluding parties, generates $t$ transcripts, so that the generated transcripts are ***distinguishable*** to that generated in the actual protocol

In general, MPC can be implemented through three different frameworks.

### Oblivious Transfer

OT is a two-party consumption protocol proposed by Rabin in 1981.

In OT, the sender owns a database of message-index pairs

$$ (M_1,1), (M_2,2), (M_3,3),...,(M_N,N)$$

At each transfer, receiver chooses an index $1 \leq i \leq N$

and receives $M_i$

The receiver doesn't learn anything other than $M_i$ about the database, and the sender doesn't know anything about the selection.

>**Definition 1-out-of-n OT**
>
>Suppose Party A has a list($x_1,...,x_n$) as input Party B has $i \in 1,...n$ as input. 1-out-of-n OT is an MPC protocol where A learns nothing about $i$ and B learns nothing but $x_i$

When n=2, we get 1-out-of-2 OT which has the following property: 1-out-of-2 OT is universal for 2-party MPC. That is, given a 1-out-of-2 OT protocol, one can conduct any secure 2-party computation.

> ***The Bellare-Micali Construction***
>
> The receiver sends 2 public keys to the sender. The receiver only holds one public key corresponding to one of the 2 public keys, and the sender does not know which public key it is. Then, the sender encrypts the two messages with their corresponding public keys, and sends the ciphertexts to the receiver. Finally, the receiver decrypts the target ciphertext with the private key.
>
> In a discrete logarithm setting $(\mathbb G, g, p)$, where $\mathbb G$ is a group of prime order $p, g \in \mathbb G$ is a generator, and $H : G \rightarrow \{0, 1\}^n$ is a hash function, Suppose the ==sender A== has $x_0, x_1 \in \{0, 1\}^n $ , and the ==receiver B== has $b \in \{0,1\}$
>
> 接收者向发送者发送了两个公钥。接收者只持有与这两个公钥中的一个对应的公钥，而发送者不知道是哪一个公钥。然后，发送者使用它们对应的公钥对两条消息进行加密，并将密文发送给接收者。最后，接收者使用私钥解密目标密文。
>
> 在离散对数设置中$(\mathbb G, g, p)$，其中$\mathbb G$是一个素数阶$p$的群，$g \in \mathbb G$是一个生成元，$H : G \rightarrow {0, 1}^n$是一个哈希函数。假设发送者A有$x_0, x_1 \in {0, 1}^n$，而接收者B有$b \in {0,1}$。
>
> 1. $\mathcal A$ chooses a random element $c \leftarrow G$ and sends it to $\mathcal B$
>
> 2. $\mathcal B$ chooses $k \leftarrow \mathbb Z_p$ and sets $PK_b = g^k$, $PK_{1-b} = c/PK_b$, then sends $PK_0$ to $\mathcal B$. 
>
>    $\mathcal B$ sets $PK_1 = c/PK_0$ 
>
> 3. $\mathcal A$ encrypts $x_0$ with ElGamal scheme using $PK_0$ (i.e., setting $ C_0 = [g^{r_0}, HASH(PK_0) * x_0]$ ). Then, $\mathcal A$ sends $(C_0, C_1)$ to $\mathcal B$
>
> 4. $\mathcal B$ decrypts $C_b$ using private key $k$ to obtain $x_b = PK_b^{r_b} * x_b / g^{r_bk}$

[ElGamal加密算法](https://zh.m.wikipedia.org/zh-hans/ElGamal%E5%8A%A0%E5%AF%86%E7%AE%97%E6%B3%95)

### Secret Sharing

Secret sharing is a concept of hiding a secret value by splitting it into random parts and distributing these parts (a.k.a. shares) to different parties, so that each party has only one share and thus only one piece of the secret.

There are several types of secret sharing, mainly including arithmetic secret sharing, Shamir's secret sharing and binary secret sharing.

Here we focus on arithmetic secret sharing.

Consider that a party $P_i$ wants to share a secret $S$ among $n$ parties $\{P_i\}_{i=1}^n$ in a finite field $F_q$ . 

To share S, the party $P_i$ randomly samples $n-1$ values $\{s_i\}^n_{i=1}$ from $\mathbb Z_q$ and set $s_n = S - \sum_{i=1}^{n-1} s_i$  mod  $q$ 

Then, $P_i$ distributes $s_k$ to party $P_k$ for $ k \neq i$ 

We denote the shared $S$ as $<S> = \{s_i\}_{i=1}^n$

#### Shamir 秘密共享协议

>最早在1970年基于Lagrange插值和矢量方法提出的。基本思想是将秘密$s$分解成$n$个秘密，分发给持有者，其中任意不少于$t$个秘密均能恢复密文，而任意少于$t$个秘密均无法得到密文的任何信息
>
>1. 加密过程
>
>  - 假设有秘密$S$要保护，任意取$t-1$个随机数，构造如下多项式
$$
>   f(x) = a_0 + a_1x + a_2x^2+...+a_{t-1}x^{t-1}
> $$
>
>   ​       其中$a_0$是秘密$S$ 所有运算均在有限域中进行
>
>   - 取任意$n$个数，$x_1,x_2,...,x_n$分别带入多项式，得到$f(x_1),...,f(x_n)$
>
>   - 将$(x_1,f(x_1)),(x_2,f(x_2)),...,(x_n,f(x_n))$分发到$n$个服务器上
>
>2. 解密过程
>
>   ![img](https://pic3.zhimg.com/80/v2-b88ddcd7e7e35c00271a661b456d2b6e_720w.webp)
>
>   ![img](https://pic3.zhimg.com/80/v2-841b71b9fee5af96a3272888e792f1c2_720w.webp)
>
>   ![img](https://pic1.zhimg.com/80/v2-cb0eee0588b141fc0904f41257325678_720w.webp)



# Distributed Machine Learning



