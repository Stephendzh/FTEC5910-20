# Privacy Preservation Techniques

We cover 3 types of such approaches, namely (1)MPC (2) HE and (3)DP

## Secure Multi-party computation

Secure Multi-Party Computation a.k.a secure function evaluation, was initially introduced as a secure two-party computation problem.

MPC allows us to compute functions of private input value so that each party learns only the corresponding function output value, but not input values from other parties. For example, given a secret value $x$ that is split into $n$ shares so that a party $P_i$ only knows $x_i$ all party can collaborative compute

$$
y_1,...,y_n = f(x_1,...x_n)
$$
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
> 在离散对数设置中$(\mathbb G, g, p)$，其中$\mathbb G$是一个素数阶$p$的群，$g \in \mathbb G$是一个生成元，$H : G \rightarrow \{0, 1\}^n$是一个哈希函数。假设发送者A有$x_0, x_1 \in \{0, 1\}^n$，而接收者B有$b \in \{0,1\}$
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
>   - 假设有秘密$S$要保护，任意取$t-1$个随机数，构造如下多项式
>
> $$
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

### Homomorphic Encryption

HE is generally considered as an alternative approach to MPC in PPML. HE can also be used to achieve MPC as discussed in previous section.(同态加密)

#### Definition

An HE scheme $\mathcal H$ is an encryption scheme that allows certain algebraic operations to be carried out on the encrypted content, by applying an efficient operation to the corresponding ciphertext (without knowing the decryption key). An HE scheme $\mathcal H$ consists of a set of 4 functions:
$$
\mathcal H = \{KeyGen, Enc, Dec, Eval\}
$$
where

- $KeyGen$ : Key generation. A cryptograohic generator $g$ is taken as the input. For asymmetric HE, a apir of keys $\{pk, sk\} = KeyGen(g)$ are generated where $pk$ is the public key for encryption of the plaintext and $sk$ is the secret key for decryption of the ciphertext. For symmetric HE, only a secret key $sk = KeyGen(g)$ is generated.
- $Enc$ : Encryption. For asymmetric HE, an encryption scheme takes the public key $pk$ and the plaintext $m$ as input, and generates the ciphertext $c = Enc_{pk}(m)$ as the output. For symmetric HE, an HE scheme takes the secret key $sk$ and the plaintext $m$, and generates ciphertext $ c = Enc_{sk}(m)$ 

>Palliar 算法
>
>1999年发明的概率公钥加密算法，该算法基于复合剩余类的困难问题， 是一种满足假发的同态加密算法
>
>（1）密钥产生
>
>选取两个随机的大素数 $p,q$ 计算$n = p*q $ 和$\lambda = lcm(p-1, q-1)$, 其中， $ lcm(，)$是两个参数的最小公倍数

# Distributed Machine Learning



Referred as DML.

DML  can generally be categorized into 2 classes, namely the scalability-motived DML and privacy-motived DML. The scalability-motived DML refers to the DML paradigm that is designed to  address the ever-increasing scalability and computation requirements of large-scale ML systems.

For example. in the past decades, the scales of the problems  that ML and DL methods have to deal with have increased exponentially. Training a sophisticated  DL model with a huge amount of data can easily exceed the capability of the traditional MLparadigm that relies on a single computing entity. One outstanding example is the famous BERTmodel [Devlin et al., 2019], which requires multiple tensor processing units (TPUs) for pre-training and it may take several days even with a fleet of TPUs. To cope with such scenarios, the fast-developing DML methods are considered as the answer to the ever-increasing size and complexity of ML models.

##  Scalability-Motivated DML

### Large-scale machine learning

With the emergence of widespread communication and sensing devices, such as smartphones, portable gadgets, IoT sensors, and wireless cameras, data are ubiquitously available in enormous volumes. In this big data era, the bottleneck of ML methods has shifted from being able to infer from small training samples to dealing with large-scale high-dimensional datasets. With this trend shift, the ML community is faced with the challenge that the computation power and time do not scale well with the dataset size, making it impossible to learn from large-scale training samples with reasonable computation effort and time. We summarize in the following the major challenges that conventional ML methods are faced with when dealing with large-scale datasets.

Memory shortage

Unreasonable training time.

### SCALABILITY-ORIENTEDDMLSCHEMES 

Excessive research efforts have been cast on presenting effective frameworks and methods for dealing with large-scale datasets and ML models. Particularly, training large-scale DL mod els is very time-consuming, with the training period ranging from days to even weeks. More recently, numerous research works have been carried out to push the frontiers of DML, aim ing to reduce training time and cope with large-scale DL models. We review here some of the popular scalability-oriented DML schemes, covering ==data parallelism, model parallelism, graph parallelism, task parallelism, hybrid parallelism, and mixed parallelism==

## Privacy-Motived DML

 In the following, we give a quick review of representative works on privacy-preserving DML, emphasizing on how they utilize privacy protection tools mentioned above to protect the data and model security in a distributed environment. According to the aforementioned tools, we f irst summarize the DML algorithms using obfuscation and then introduce those algorithms that use cryptographic methods. 

### PRIVACY-PRESERVINGDMLSCHEMES

Chaudhuri and Monteleoni [2009] proposed a privacy-preserving logistic regression al gorithm based on DP. They tackle the optimization over randomized data, making it possible to take a balance between model performance and privacy protection and make the privacy bound tighter. Following the definition given by Dwork [2008], they prove that their work guarantees "-differential privacy, and provide a novel algorithm with better performance. In the proposed work, a randomized vector is generated using a Gamma function, which participates in the  optimization of the logistic regression parameter . Moreover, they concluded that their work reveals the relation between perturbation-based privacy protection and regularization.

Wild and Mangasarian [2007] and Mangasarian et al. [2008] studied privacy-preserving support vector machines (PPSVMs) on horizontally and vertically partitioned datasets, respectively. They concealed the originally learned kernel with a randomly generated kernel, achieving comparable performance to the non-private SVMs. The privacy proof is based on the fact that there are infinite possible input data that can be recovered from the perturbed kernel. Therefore, sharing the perturbed kernel will not cause privacy leakage. However, these methods require participants to share the randomly generated kernel, limiting the application of these methods.

 In Aonoetal. [2016], authors utilize HE to protect the data during the training of logistic regression. Their method uses a two-degree approximation to the log-linear objective function, making the training process compatible with the additive HE method, which improves compu tational efficiency while maintaining a comparable performance. Besides, they claim that their output is compatible with DP. They also analyze the storage and computation complexity of their system, showing that their system supports large-scale distributed computation. Fienberg  et al. [2006] also considered linear regression (LR) on the horizontally partitioned dataset, uti lizing MPC method to aggregate the calculation. However, in their setting, the features are categorical, which means the computation space is small. Slavkovic et al. [2007] made signifi cant progress, using secure summation protocol and secure matrix multiplication for the aggregation of distributed learning of LR, which supports both vertical and horizontal data partition.
