
# Cadastro de alunos :

# Entrada:

print('\n\n\t\t\t --Boletim Escolar--')
print('-'*60)

ra = input(f'Escreva o seu nome Para consultar o seu Boletim:')

# Cadastro dos Alunos
boletim =('Boletim do Aluno carregado!')

julia =('Nome: Julia','Nota:100','Curso:Pyhton','Aluno Aprovado!')
kauan =('Nome: Kauan','Nota:60','Curso:Pyhton','Aluno Aprovado!')
giovanni =('Nome: Giovanni','Nota:40','Curso:Pyhton','Aluno Reprovado!')
luiz =('Nome: Luiz','Nota:25','Curso:Pyhton','Aluno Reprovado!')

#Saída
print('\n\n\t--Boletim do Aluno--')
print('-'*60)
if ra == 'luiz':
    print(f'{luiz}')
if ra == 'kauan':
    print(f'{kauan}')
if ra == 'julia' and 'giovanni':
    print(f'{julia}')
if ra == 'giovanni' and 'julia':
    print(f'{giovanni}')
#    print(f'Boletim Não encontrado!')


