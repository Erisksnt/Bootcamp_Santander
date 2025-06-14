  ## Funções como objetos de primeira classe
  - Podem ser passadas e usadas como argumentos
  - Exemplo:
    ```python
    def do_something(name):
        # code...
        return ...
    
    # Utilizando
    do_something(arg)
    ```

  ## Funções internas (Inner Functions)
  - É possível definir funções dentro de funções
  - Exemplo:
    ```python
    def pai():
        print("oi")
        
        def filho():
            return "tchau"
        
        filho()
    
    pai()
    ```

  ## Decoradores
  - Adicionam comportamentos antes de executar uma função
  - Exemplo:
    ```python
    def decorador(func):
        def wrapper():
            print("Antes da execução")
            func()
            print("Depois da execução")
        return wrapper
    
    @decorador
    def exemplo():
        print("Função decorada")
    ```

  ## Introspecção
  - Capacidade de examinar objetos em runtime
  - Métodos úteis:
    ```python
    dir(), type(), hasattr(), getattr()
    ```

  ## Iteradores
  - Objetos com métodos `__iter__()` e `__next__()`
  - Exemplo:
    ```python
    class Contador:
        def __init__(self, limite):
            self.limite = limite
        
        def __iter__(self):
            self.atual = 0
            return self
        
        def __next__(self):
            if self.atual < self.limite:
                self.atual += 1
                return self.atual
            raise StopIteration
    ```

  ## Geradores
  - Funções com `yield` que retornam iteradores
  - Exemplo:
    ```python
    def gerador_pares(max):
        n = 0
        while n < max:
            yield n
            n += 2
    ```

  ## Regras de Uso
  ```markdown
  | Quando usar          | Tipo       | Vantagens               |
  |----------------------|------------|-------------------------|
  | Fluxo simples        | Gerador    | Menos memória           |
  | Lógica complexa      | Iterador   | Mais controle           |