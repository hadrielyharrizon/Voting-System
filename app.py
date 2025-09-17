import random

print("SISTEMA DE VOTAÇÃO")

candidates = ["Maria", "João", "Carlos", "Fernanda"]
votes = {candidate: 0 for candidate in candidates}

def show_candidates(candidate_list=None):
    if candidate_list is None:
        candidate_list = candidates
    print("\n Candidatos: ")
    for i, candidate in enumerate(candidates, 1):
        print(f'`{i}. {candidate}')
        
def vote(number, candidate_list=None):
    if candidate_list is None:
        candidate_list = candidates

    if 1 <= number <= len(candidates):
        chosen = candidates[number - 1]
        votes[chosen] += 1
        print(f'Voto resgistrado para: {chosen}.')
    else:
        print('Insira um número válido.')


def check_winner():
    max_votes = max(votes.values())
    winners = [c for c, v in votes.items() if v == max_votes]
    return winners, max_votes
    
def results():
    print('\n RESULTADO FINAL')
    for candidate, qty in votes.items():
        print(f'{candidate}: {qty} votes')

    winners, max_votes = check_winner()
    
    while len(winners) > 1:
        print(f'Empate entre {', '.join(winners)} com {max_votes} votos cada.')
        print('Vamos para a votação de desempate entre os empatados. \n')
    
        for c in winners:
            votes[c] = 0

        while True:
            show_candidates(winners)
            choice = input('Vote novamente para desempatar ("fim" para encerrar): ')
            if choice.lower() == 'fim':
                break
            elif choice.isdigit():
                vote(int(choice), winners)
            else:
                print('Insira um número válido.')

        winners, max_votes = check_winner()

    print(f'\n Vencedor Final: {winners[0]} com {max_votes} votos.')

while True:
    show_candidates()
    choice = input("Em qual candidato deseja votar? ('fim' para encerrar):")

    if choice.lower() == "fim":
        break
    elif choice.isdigit():
        vote(int(choice))
    else: 
        print('Insira um número válido.')

results()