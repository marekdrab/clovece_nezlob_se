"""
n=rozmer hracej plochy
m=počet pozícii domčeka ( ak n=9, tak m=3 čo znamená, že berieme do úvahy 3. riadok/stlpec
  v podmienkach pre pohyb)
k=najväčší počet "*" vedľa seba v riadku (použité pri generovaní hracej plochy)
r1,r2,r3,r4=riadky v hracej ploche
r5=riadok plný medzier potrebný pre pohyb
sach=samotná hracia plocha (neskôr používané ako: s)
x_cur=aktualna suradnica riadka
y_cur=aktualna suradnica stlpca
x_next=ďalšia suradnica riadka
y_next=ďalšia suradnica stlpca
step_count=zostavajuci počet riadkov (potrebné pre vyhadzovanie)
x=súradnica riadka hráča A
y=súradnica stĺpca hráča A
xb=súradnica riadka hráča B
yb=súradnica stĺpca hráča B
ha=hod kockou hráča A
hb=hod kockou hráča B
sur_A=súradnice hráča A zapísané v liste + počet figuriek v domčeku + súradnica riadka v domčeku
sur_B=súradnice hráča B zapísané v liste + počet figuriek v domčeku + súradnica riadka v domčeku
"""
n=int(input("Zadaj velkost pola, musi byt neparne a vacsie ako 5: "))
if n%2==0:
    print("Zadal si parne cislo")
if n<5:
    print("Zadal si cislo mensie ako 5")
#--------------------------------------------------------------------------------------------------------------
m=(n-3)//2
k=(n-1)//2
def gensachovnicu(n):
    m=(n-3)//2
    k=(n-1)//2
    r1=[]
    r2=[]
    r3=[]
    r4=[]
    r5=[]
    sach=[]
    
    #vytvori prvy a posledny riadok sachovnice
    for i in range(m):
        r1.append(" ")
    for i in range(3):
        r1.append("*")
    for i in range(m):
        r1.append(" ")
    r1.append(" ")
      
    #vytvori riadok ramena
    for i in range(m):
        r2.append(" ")
    r2.append("*")
    r2.append("D")
    r2.append("*")
    for i in range(m):
        r2.append(" ")
    r2.append(" ")

    #vytvori riadok s * a jednym D
    for i in range(k):
        r3.append("*")
    r3.append("D")
    for i in range(k):
        r3.append("*")
    r3.append(" ")

    #vytvori riadok s X
    r4.append("*")
    for i in range(m):
        r4.append("D")
    r4.append("x")
    for i in range(m):
        r4.append("D")
    r4.append("*")
    r4.append(" ")

    #vytvori prazdny riadok s medzerami 
    for i in range(n):
        r5.append(" ")
    
    #samotna hracska plocha
    sach.append(r1.copy())
    for i in range(m-1):
        sach.append(r2.copy())
    sach.append(r3.copy())
    sach.append(r4.copy())
    sach.append(r3.copy())
    for i in range(m-1):
        sach.append(r2.copy())
    sach.append(r1.copy())
    sach.append(r5.copy())
    
    return sach
#-------------------------------------------------------------------------------------------
#vypíš hráčov na plochu a tlačí šachovnicu

s = gensachovnicu(n)

#začiatočné súradnice A
x=0
y=m+2

#začiatočné súradnice B
xb=n-1
yb=m

#priradenie A a B na svoje pozície
s[x][y]="A"
s[n-1][m]="B"

#priradenie hodnot pre suradnice hráč A a B
sur_A=[x,y]
sur_B=[xb,yb]

#tlačenie šachovnice
def tlacsachovnicu(n):
    for i in s:
         print(" ".join(map(str,i)))

#-------------------------------------------------------------------------------------------
#hod kockou hráč A a hráč B

import random

def krokA():
    hodA=random.randint(1,6)
    return hodA

def krokB():
    hodB=random.randint(1,6)
    return hodB

#-------------------------------------------------------------------------------------------
#funkcie pre vyhadzovanie a pohyb


#funkcia pre vyhodenie
def vyhod(x_cur,y_cur,x_next,y_next, hrac_na_vyhodenie,s):
    global n,m,sur_A,sur_B
    s[x_cur][y_cur]="*"
    if hrac_na_vyhodenie == "B":
        s[x_next][y_next]="A"
        sur_B[0]=n-1
        sur_B[1]=m
        s[sur_B[0]][sur_B[1]]="B"
    else:
        s[x_next][y_next]="B"
        sur_A[0]=0
        sur_A[1]=m+2
        s[sur_A[0]][sur_A[1]]="A"


#funkcia pre pohyb
def krok(x_cur,y_cur,x_next,y_next, hybajuci_sa_hrac, nehybajuci_sa_hrac,s,step_count):
    if (s[x_next][y_next] == nehybajuci_sa_hrac):
        #ak nastane vyhodenie 
        if (step_count == 1):
            vyhod(x_cur,y_cur,x_next,y_next,nehybajuci_sa_hrac,s)
        else:
            if (s[x_next][y_next]==nehybajuci_sa_hrac):
                s[x_cur][y_cur]="*"     
    else:
        if s[x_cur][y_cur] == nehybajuci_sa_hrac: 
            s[x_next][y_next] = hybajuci_sa_hrac
        else:
            s[x_cur][y_cur] = "*"
            s[x_next][y_next] = hybajuci_sa_hrac

#------------------------------------------------------------------------------------------- 
#pohyb hráča A
            
pocet_v_domceku_A=0
x_domcek_A=m

def pohyb(s,x,y,ha,n,sur_A,pocet_v_domceku_A,x_domcek_A):
    m=(n-3)//2
    k=(n-1)//2
    for i in range(ha):
        # pohyb hráča do domčeka a vypísanie novej figúrky
        if s[0][m+1]=="A":
            pocet_v_domceku_A+=1
            print("Hráč má A v domčeku",pocet_v_domceku_A,"figuriek.")
            s[x_domcek_A][m+1]="A"
            x_domcek_A-=1
            s[0][m+1]="*"
            if pocet_v_domceku_A<m:
                s[0][m+1]="*"
                s[0][m+2]="A"
                x=0
                y=m+2
                break
            else:
                break
            
        #otočenie hráča v dolnej polovici smerom hore
        elif x==n-1 and y==m:
            krok(x,y,x-1,y,"A","B",s,ha-i)
            x-=1
            
        #otočenie hráča v pravej polovici smerom dole
        elif x==m+2 and y==m+2:
            krok(x,y,x+1,y,"A","B",s,ha-i)
            x+=1
            
        #otočenie hráča v hornej polovici smerom doprava
        elif x==m and y==m+2:
            krok(x,y,x,y+1,"A","B",s,ha-i)
            y+=1
            
        #otočenie hráča v pravej polovici smerom dole
        elif x==m and y==n-1:
            krok(x,y,x+1,y,"A","B",s,ha-i)
            x+=1
            
        #otočenie hráča v pravej polovici smerom doľava
        elif x==m+2 and y==n-1:
            krok(x,y,x,y-1,"A","B",s,ha-i)
            y-=1
            
        #otočenie hráča v dolnej polovici smerom doľava
        elif x==n-1 and y==m+2:
            krok(x,y,x,y-1,"A","B",s,ha-i)
            y-=1
            
        #otočenie hráča v ľavej polovici smerom doľava
        elif x==m+2 and y==m:
            krok(x,y,x,y-1,"A","B",s,ha-i)
            y-=1
            
        #otočenie hráča v ľavej polovici smerom hore
        elif x==m+2 and y==0:
            krok(x,y,x-1,y,"A","B",s,ha-i)
            x-=1
            
        #otočenie hráča v ľavej polovici smerom doprava
        elif x==m and y==0:
            krok(x,y,x,y+1,"A","B",s,ha-i)
            y+=1
            
        #otočenie hráča v ľavej polovici smerom hore
        elif x==m and y==m:
            krok(x,y,x-1,y,"A","B",s,ha-i)
            x-=1
            
        #pohyb hráča doľava v spodnom ramene
        elif x==n-1 and y==m+1:
            krok(x,y,x,y-1,"A","B",s,ha-i)
            y-=1
            
        #pohyb dolava v dolnej polovici
        elif (x==n-1 or x==m+2) and y!=0:
            if y>m+2 or 0<y<=m:
                krok(x,y,x,y-1,"A","B",s,ha-i)
                y-=1
                
        #pohyb doprava v hornej polovici
        elif x==m and (y!=m or y!=n-1):
            krok(x,y,x,y+1,"A","B",s,ha-i)
            y+=1
            
        #pohyb dole v pravej polovici
        elif (y==m+2 or y==n-1) and (x!=m or x!=m+2 or x!=n-1):
            krok(x,y,x+1,y,"A","B",s,ha-i)
            x+=1
            
        #pohyb hráča doprava v hornom ramene
        elif x==0 and y==m:
            krok(x,y,x,y+1,"A","B",s,ha-i)
            y+=1
            
        #pohyb hore v lavej polovici
        elif (y==0 or y==m) and (x!=m+2 or x!=m or x!=0):
            krok(x,y,x-1,y,"A","B",s,ha-i)
            x-=1

    print()
    return [x,y,pocet_v_domceku_A,x_domcek_A]

#-------------------------------------------------------------------------------------------
#pohyb hráča B po ploche


pocet_v_domceku_B=0
x_domcek_B=m+2

def pohyb_B(s,xb,yb,hb,n,sur_B,pocet_v_domceku_B,x_domcek_B):
    m=(n-3)//2
    k=(n-1)//2
    for i in range(hb):
        #pohyb hráča do domčeka a vypísanie novej figúrky
        if xb==n-1 and yb==m+1:
            pocet_v_domceku_B+=1
            print("Hráč B má v domčeku",pocet_v_domceku_B,"figuriek.")
            s[x_domcek_B][m+1]="B"
            x_domcek_B+=1
            s[n-1][m+1]="*"
            if pocet_v_domceku_B<m:
                s[n-1][m+1]="*"
                s[n-1][m]="B"
                xb=n-1
                yb=m
                break
            else:
                break
        
        #otočenie hráča v hornej polovici smerom doprava
        elif xb==0 and yb==m:
            krok(xb,yb,xb,yb+1,"B","A",s,hb-i)
            yb+=1
            
        #otočenie hráča v hornej polovici smerom dole
        elif xb==0 and yb==m+2:
            krok(xb,yb,xb+1,yb,"B","A",s,hb-i)
            xb+=1
            
        #otočenie hráča v ľavej polovici smerom doprava
        elif xb==m and yb==0:
            krok(xb,yb,xb,yb+1,"B","A",s,hb-i)
            yb+=1
            
        #otočenie hráča v ľavej polovici smerom hore
        elif xb==m and yb==m:
            krok(xb,yb,xb-1,yb,"B","A",s,hb-i)
            xb-=1
            
        #otočenie hráča v pravej polovici smerom doprava
        elif xb==m and yb==m+2:
            krok(xb,yb,xb,yb+1,"B","A",s,hb-i)
            yb+=1
            
        #otočenie hráča v pravej polovici smerom dole
        elif xb==m and yb==n-1:
            krok(xb,yb,xb+1,yb,"B","A",s,hb-i)
            xb+=1
            
        #otočenie hráča v ľavej polovici smerom hore
        elif xb==m+2 and yb==0:
            krok(xb,yb,xb-1,yb,"B","A",s,hb-i)
            xb-=1
            
        #otočenie hráča v dolnej polovici smerom doľava
        elif xb==m+2 and yb==m:
            krok(xb,yb,xb,yb-1,"B","A",s,hb-i)
            yb-=1
            
        #otočenie hráča v dolnej polovici smerom dole
        elif xb==m+2 and yb==m+2:
            krok(xb,yb,xb+1,yb,"B","A",s,hb-i)
            xb+=1
            
        #otočenie hráča v pravej polovici smerom doľava
        elif xb==m+2 and yb==n-1:
            krok(xb,yb,xb,yb-1,"B","A",s,hb-i)
            yb-=1
            
        #otočenie hráča v dolnej polovici smerom hore
        elif xb==n-1 and yb==m:
            krok(xb,yb,xb-1,yb,"B","A",s,hb-i)
            xb-=1
            
        #otočenie hráča v dolnej polovici smerom doľava
        elif xb==n-1 and yb==m+2:
            krok(xb,yb,xb,yb-1,"B","A",s,hb-i)
            yb-=1
            
        #pohyb hore v lavej polovici
        elif (yb==0 or yb==m) and (xb!=m+2 or xb!=m or xb!=0):
            krok(xb,yb,xb-1,yb,"B","A",s,hb-i)
            xb-=1
            
        #pohyb dolava v dolnej polovici
        elif (xb==n-1 or xb==m+2) and yb!=0:
            if yb>m+2 or 0<yb<=m:
                krok(xb,yb,xb,yb-1,"B","A",s,hb-i)
                yb-=1
                
        #pohyb dole v pravej polovici
        elif (yb==m+2 or yb==n-1) and (xb!=0 or xb!=m+2 or xb!=n-1):
            krok(xb,yb,xb+1,yb,"B","A",s,hb-i)
            xb+=1
            
        #pohyb doprava v hornej polovici
        elif (xb==m or xb==0) and (yb!=m or yb!=n-1):
            krok(xb,yb,xb,yb+1,"B","A",s,hb-i)
            yb+=1

    print()
    return [xb,yb,pocet_v_domceku_B,x_domcek_B]

#-------------------------------------------------------------------------------------------
#Hra dvoch hráčov 

print("Máte ",(n-3)//2,"panáčikov")
tlacsachovnicu(n)
print()

while True:
    if pocet_v_domceku_A==m:
        print("Hráč A vyhral hru")
        break
    elif pocet_v_domceku_B==m:
        print("Hráč B vyhral hru")
        break
    ha=krokA()
    hb=krokB()
    vstup_pre_krok=input("Pre pokračovanie stlač ENTER: ")
    print("Hráč A hodil: ",ha)
    sur_A=pohyb(s,x,y,ha,n,sur_A,pocet_v_domceku_A,x_domcek_A)
    tlacsachovnicu(n)
    vstup_pre_krok_1=input("Pre pokračovanie stlač ENTER: ")
    print("Hráč B hodil: ",hb)
    sur_B=pohyb_B(s,xb,yb,hb,n,sur_B,pocet_v_domceku_B,x_domcek_B)
    tlacsachovnicu(n)
    x=sur_A[0]
    y=sur_A[1]
    pocet_v_domceku_A=sur_A[2]
    x_domcek_A=sur_A[3]
    xb=sur_B[0]
    yb=sur_B[1]
    pocet_v_domceku_B=sur_B[2]
    x_domcek_B=sur_B[3]






