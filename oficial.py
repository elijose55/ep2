import random
import time
import json




with open('arquivo.json','r') as cf:
    jogo=json.load(cf)
    
n=jogo['jogador']['player']['nome']
print('Bem Vindo ao Inspermon')
print('Seu inspermon é o {0}' .format(n))
print('\n')
    
p=[]
for i in jogo['pokemon']:
    p.append(jogo['pokemon'][i]['nome'])
    
l=len(p)



def loja():
        n=jogo['jogador']['player']['nome']
        cr=jogo['jogador']['player']['creditos']
        print('Bem Vindo a Loja')
        print('Créditos: {0}' .format(jogo['jogador']['player']['creditos']))
        print('\n'*2)
        time.sleep(0.5)
        print('1 - Bau da sorte - 20 créditos' ,end='\n'*2 )
        print('2 - Trocar nome de {0} - 50 créditos ' .format(n) ,end='\n'*2 )
        print('3 - Evoluir {0} - 60 créditos' .format(n) ,end='\n'*2)
        print('4 - Time-Bonus' ,end='\n'*2 )
        print('5 - Voltar')
        d=int(input('O que deseja obter? '))
        print('\n')

        
        if d==4: 
            tr=time.clock()-jogo['jogador']['player']['tempo']
            if jogo['jogador']['player']['tempo']==0:
                print('Você coletou seu Time-Bonus de 15 créditos!')
                print('Volte daqui a 10 minutos para coletar novamente!')
                jogo['jogador']['player']['creditos']+=15
                jogo['jogador']['player']['tempo']=time.clock() 
                
            elif tr>=600:
                print('Você coletou seu Time-Bonus de 15 créditos!')
                print('Volte daqui a 10 minutos para coletar novamente!')
                jogo['jogador']['player']['creditos']+=15
                jogo['jogador']['player']['tempo']=time.clock()
            else:
                ty=600-tr
                tx=ty//60
                print('Falta ainda {0} minutos para voce receber o proximo bonus...' .format(tx))
                
        
        if d==1:
            if cr>=20:
                jogo['jogador']['player']['creditos']-=20
                g=random.randint(9,100)
                if g==9 or g==11 or g==12 or g==13 or g==14 or g==15 or g==16 or g==17:
                    print('Você ganhou uma troca de nome para {0}!' .format(n))
                    print('\n'*2)
                
                
                elif g==10 or g==18 or g==19 or g==20 or g==21 or g==22 or g==23 or g==24:
                    print('Voce ganhou uma evolução para {0}!' .format(n))
                    print('\n'*2)
                    jogo['jogador']['player']['vida']+=5
                    jogo['jogador']['player']['defesa']+=5
                    jogo['jogador']['player']['poder']+=5
                    jogo['jogador']['player']['classe']+=1
                    print('{0} é agora um inspermon de classe {1}' .format(n,jogo['jogador']['player']['classe']))
                    print('\n'*2)
                
                
                else:
                    print('Você ganhou {0} créditos!' .format(g))
                    jogo['jogador']['player']['creditos']+=g
                        
            else:
                print('Você não tem créditos suficientes...')

        if d==2:
            if cr>=50:
                new=str(input('Qual seria o novo nome de {0}? ' .format(n)))
                print('{0} se chama agora {1}!' .format(n,new))
                jogo['jogador']['player']['nome']=new
                n=jogo['jogador']['player']['nome']
                jogo['jogador']['player']['creditos']-=50
            else:
                print('Você não tem créditos suficientes...')
            
        if d==3:
            if cr>=60:
                jogo['jogador']['player']['vida']+=5
                jogo['jogador']['player']['defesa']+=5
                jogo['jogador']['player']['poder']+=5
                jogo['jogador']['player']['classe']+=1
                print('{0} é agora um inspermon de classe {1}' .format(n,jogo['jogador']['player']['classe']))
                print('\n'*2)
                jogo['jogador']['player']['creditos']-=60
            else:
                print('Você não tem créditos suficientes...')
                
                
                
                
                
                
def dormir():
        s=0
        print('1 - Sim  |  2 - Não  |  3 - Voltar')
        fh=int(input('Você quer salvar?'))
        if fh==1:
            with open('arquivo.json','w') as file:
                json.dump(jogo, file, indent=1)
            print('Até a próxima!!')
            s=1

        if fh==2:
            print('Até a próxima!!')
            s=1
        return s

        
    





def index():
            print('             Insperdex', end='\n'*3)
            print('Meu Inspermon: {0}' .format(jogo['jogador']['player']['nome']))
            print('Poder: {0}' .format(jogo['jogador']['player']['poder']))
            print('Vida: {0}' .format(jogo['jogador']['player']['vida']))
            print('Defesa: {0}' .format(jogo['jogador']['player']['defesa']))
            print('Classe: {0}' .format(jogo['jogador']['player']['classe']))
            print('Experiência: {0}' .format(jogo['jogador']['player']['experiencia']))
            print('Experiência para evoluir: {0}' .format(jogo['jogador']['player']['experiencia para evoluir']))
            print('\n'*2)
            for i, h in (jogo['jogador']['insperdex']).items():
                print(i)
                ir=i
                print('Poder: {0}' .format(jogo['jogador']['insperdex'][ir]['poder']))
                print('Vida: {0}' .format(jogo['jogador']['insperdex'][ir]['vida']))
                print('Defesa: {0}' .format(jogo['jogador']['insperdex'][ir]['defesa']) , end='\n'*2)
                
                
                
                
def find():
            h=random.randint(0,(l-1))
            h+=1
            h=str(h)
            encontrado=jogo['pokemon'][(h)]['nome']     #nome do pokemon encontrado
            return encontrado,h
            
    
def novo(h,encontrado):            
    if encontrado in jogo['jogador']['insperdex']:
                print('Você encontrou um {0}!' .format(encontrado))
    else:
                jogo['jogador']['insperdex'][encontrado]=jogo['pokemon'][(h)]
                print('Novo inspermon encontrado!!')
                time.sleep(0.2)
                print('.', end='')
                time.sleep(0.2)
                print('.', end='')
                time.sleep(0.2)
                print('.')
                time.sleep(0.3)
                print('É um {0}' .format(encontrado))
                time.sleep(0.4)
                print('\n'*3)

def fuga():
            print("1 - Sim  |  2 - Nao")
            q=int(input('Você quer fugir? '))
            print('\n')
            time.sleep(0.2)
            print('.', end='')
            time.sleep(0.2)
            print('.', end='')
            time.sleep(0.2)
            print('.')
            time.sleep(0.3)
            if q==1:
                a=random.randint(0,1)
                if a==0:
                    print('Fuga bem-sucedida!')
                    time.sleep(0.3)
                    print('Empate...')
                    print('\n'*1)
                    print('Você não ganhou experiência...')
                    time.sleep(0.7)
                    q=1
                else:
                    print('Fuga mal-sucedida...')
                    time.sleep(0.3)
                    print('\n'*1)
                    print('Você perdeu uma rodada de ataque...')
                    print('\n'*1)
                    time.sleep(0.4)
                    q=0
            return q    
                    
                
                
def batalha():
    
            encontrado,h=find()
            
            novo(h,encontrado)
            
            q=fuga()

            n=jogo['jogador']['player']['nome']           #nome do seu pokemon            
            v=jogo['jogador']['player']['vida']     #vida sua
            vi=jogo['pokemon'][(h)]['vida']      #vida do inimigo
            a=jogo['jogador']['player']['poder']     #ataque seu
            ai=jogo['pokemon'][(h)]['poder']      #ataque do inimigo
            d=jogo['jogador']['player']['defesa']     #defesa sua
            di=jogo['pokemon'][(h)]['defesa']      #defesa do inimigo
            
            w=random.uniform(0.75, 1.25)
            if q==2:      #nao quis fugir
                print('Começa a batalha!')
                print('\n'*1)
                time.sleep(1)
                while vi>0 and v>0:
                    vi=vi-((a*w)-di)
                    if vi<=0:
                        print('{0} ganhou!' .format(n), end='\n'*2)
                        print('\n'*1)
                        time.sleep(0.5)
                        print('{0} ganhou 3 pontos de experiência!'.format(n), end='\n'*5)
                        print('\n'*1)
                        time.sleep(0.9)
                        jogo['jogador']['player']['experiencia']+=3
                        break
                    v=v-((ai*w)-d)
                    if v<=0:
                        print('{0} perdeu...' .format(n), end='\n'*2)
                        print('\n'*1)
                        time.sleep(0.5)
                        print('{0} ganhou 1 ponto de experiência!'.format(n), end='\n'*5)
                        print('\n'*1)
                        time.sleep(0.9)
                        jogo['jogador']['player']['experiencia']+=1
                        break

            if q==0:            #quis fugir mas nao deu  
                print('Começa a batalha!')
                print('\n'*1)
                time.sleep(1)
                while vi>0 and v>0:
                    v=v-((ai*w)-d)
                    if v<=0:
                        print('{0} perdeu...' .format(n), end='\n'*2)
                        print('\n'*1)
                        time.sleep(0.5)
                        print('{0} ganhou 1 ponto de experiência!' .format(n), end='\n'*5)
                        print('\n'*1)
                        time.sleep(0.9)
                        jogo['jogador']['player']['experiencia']+=1
                        break
                    vi=vi-((a*w)-di)
                    if vi<=0:
                        print('{0} ganhou!' .format(n), end='\n'*2)
                        print('\n'*1)
                        time.sleep(0.5)
                        print('{0} ganhou 3 pontos de experiência!'.format(n), end='\n'*5)
                        print('\n'*1)
                        time.sleep(0.9)
                        jogo['jogador']['player']['experiencia']+=3
        
            if q==1:
                print('\n'*5)
    
    
    
    
        


def experiencia():    
    if (jogo['jogador']['player']['experiencia']) >= (jogo['jogador']['player']['experiencia para evoluir']):
        ee=jogo['jogador']['player']['experiencia para evoluir']
        print('{0} tem experiência suficiente para evoluir!'.format(n))
        print("1 - Evoluir  |  2 - Obter Créditos ")
        s=int(input('Gostaria de evoluir ou obter {0} créditos?'.format(ee/3)))
        if s==1:
            jogo['jogador']['player']['vida']+=5
            jogo['jogador']['player']['defesa']+=5
            jogo['jogador']['player']['poder']+=5
            jogo['jogador']['player']['classe']+=1
            jogo['jogador']['player']['experiencia']-=ee
            jogo['jogador']['player']['experiencia para evoluir']+=15
            print('{0} é agora um inspermon de classe {1}' .format(n,jogo['jogador']['player']['classe']))
        if s==2:
            jogo['jogador']['player']['creditos']+=(ee/3)
            jogo['jogador']['player']['experiencia']-=ee
            print('Você tem {0} créditos' .format( jogo['jogador']['player']['creditos']))
    return








while True:
    
    experiencia()
    
    n=jogo['jogador']['player']['nome']
    
    print('\n'*2)
    print("1 - Passear  |  2 - Dormir  |   3 - Acessar Insperdex  |  4 - Loja  |  5 - Salvar ")
    x=int(input('Digite o número da sua próxima jogada: '))
    print('\n'*3)
    
    
    
    if x==1:
        batalha()
        
    if x==2:
        s=dormir()
        if s==1:
            break

    
    if x==3:
        index()
        
    if x==4:
        loja()
        
    if x==5:
        with open('arquivo.json','w') as file:
            json.dump(jogo, file, indent=1)
        print('Jogo salvo!')
        
        
