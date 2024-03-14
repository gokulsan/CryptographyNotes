NTRU encryption and decryption methods are different. The encryption procedure uses a mixing system based on polynomial algebra and reduction modulo two numbers p and q, while the decryption procedure uses an unmixing system whose validity depends on elementary probability theory. 

An NTRU cryptosystem depends on three integer parameters (N,p, q) and four sets of polynomials of degree N- 1 with 
integer coefficients. Note that p and q need not be prime, but we will assume that gcd(p, q) = 1, and q will always be considerably larger than p. 

The security of the NTRU public key cryptosystem comes from  the interaction of the polynomial mixing system with the independence of reduction modulo p and q. Security also relies on the fact that for most lattices, it is very difficult to find extremely short vectors. 
