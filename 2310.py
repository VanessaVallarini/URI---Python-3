N=int(input())
sum_s=0
sum_b=0
sum_a=0
sum_s1=0
sum_b1=0
sum_a1=0
p_s = 0
p_b = 0
p_a = 0

for i in range(N):
    jogador=input()
    s,b,a=map(float,input().split())
    s1,b1,a1=map(float,input().split())
    sum_s += s
    sum_b += b
    sum_a += a
    sum_s1 +=s1
    sum_b1 += b1
    sum_a1 += a1

p_s = (sum_s1/sum_s)*100.00
p_b = (sum_b1/sum_b)*100.00
p_a = (sum_a1/sum_a)*100.00

print("Pontos de Saque: %.2f" %p_s,"%.")
print("Pontos de Bloqueio: %.2f" %p_b,"%.")
print("Pontos de Ataque: %.2f" %p_a,"%.")
