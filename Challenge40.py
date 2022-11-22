''' Challenge 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado!;
- Média entre 5.0 e 6.9: Recuperação!;
- Média 7.0 ou superior: Aprovado!; '''

import emoji
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média foi {media:.1f}. Você está reprovado!')
    print(emoji.emojize('QUE TRISTEZA :sob:', language='alias'))
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média foi {media:.1f}. Você está de recuperação!')
    print(emoji.emojize('POXA :unamused:', language='alias'))
else:
    print(f'Sua média foi {media:.1f}. Você foi aprovado!')
    print(emoji.emojize('PARABÉNS :sunglasses:', language='alias'))
