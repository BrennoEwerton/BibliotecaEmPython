class Biblioteca:
    def __init__(self, listaDeLivros):
        self.livros = listaDeLivros

class Biblioteca:
    def __init__(self, listaDeLivros):
        self.livros = listaDeLivros

    def exibirLivrosDisponiveis(self):
        print("\nOs livros disponíveis nessa biblioteca são: \n")
        for livro in self.livros: 
            print(" * " + livro)
    
    def livrosEmprestados(self, nomeLivro):
        if nomeLivro in self.livros:
            print(f"\nVocê pegou emprestado o livro {nomeLivro}. Devolva em um prazo de até 30 dias.")
            self.livros.remove(nomeLivro)
            return True
        else:
            print("\nDesculpa, esse livro não está disponível na Central dos Livros. Por favor, escolha outro livro disponível.")
            return False

    def devolucaoLivro(self, nomeLivro):
        self.livros.append(nomeLivro)
        print("\nObrigado por devolver esse livro!")

class Estudante: 
    def solicitarLivro(self):
        self.livros = input("Digite o nome do livro que você quer pegar emprestado: ")
        return self.livros

    def devolucaoLivro(self):
        self.livros = input("Digite o nome do livro que você quer devolver: ")
        return self.livros
         

if __name__ == "__main__":
    centraldoslivros = Biblioteca(["Senhor dos aneis", "O hobbit", "Assim falou Zaratustra", "Misto quente", "Sobre a brevidade da vida", "Código limpo", "1984"])
    estudante = Estudante()
   
    while(True):
        msgBoasVindas = '''\n ====== Central dos Livros ======
        Escolha um opção:
        1. Exibir todos os livros
        2. Pegar livro emprestado
        3. Devolver livro
        4. Sair 
        '''
        print(msgBoasVindas)
        a = int(input("Escolha uma opção: "))
        if a == 1:
            centraldoslivros.exibirLivrosDisponiveis()
        elif a == 2:
            centraldoslivros.livrosEmprestados(estudante.solicitarLivro())
        elif a == 3:
            centraldoslivros.devolucaoLivro(estudante.devolucaoLivro())
        elif a == 4:
            print("\nObrigado por escolher a Central dos Livros. Tenha um bom dia!")
            exit()
        else:
            print("\nOpção inválida!")