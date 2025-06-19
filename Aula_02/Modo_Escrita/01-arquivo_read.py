#Estrutura para achar o caminho do arquivo é (r"caminho_do_arquivo", "r")
#Esse "r" no começo da estrutura diz para o phyton "Não interprete barras invertidas como comandos especiais".

arquivo = open(
    r"C:\Users\Erick\OneDrive\Documentos\Bootcamp_Santander\Aula_02\Modo_Escrita\teste.txt", "w"
)
arquivo.write('Escrevendo dados em um novo arquivo.') #Escrevendo algo para colocar dentro do arquivo criado
arquivo.writelines(['escrevendo', 'um', 'novo','Phyton']) #Escrevendo item a item para colocar no arquivo.
arquivo.close()

