# Produtorio-Somatorio.NiCoding

Este repositório contém os códigos-fontes desenvolvidos para o **Episódio 2** do seriado **NiCoding**, focado na implementação e compreensão matemática dos conceitos de **Somatório** e **Produtório** utilizando a linguagem **Python**.

---

## 📺 Sobre o seriado NiCoding

O **NiCoding** é uma série prática e didática de projetos em programação voltada para o aprendizado progressivo de conceitos da lógica de programação e matemática computacional. Cada episódio aborda a implementação de soluções de forma acessível e direta ao ponto.

---

## 📌 Sobre o Projeto (EP2)

O objetivo deste episódio é resolver dois conceitos matemáticos fundamentais utilizando estruturas de repetição (`while`) com variáveis contadoras e acumuladoras:

### 1. Somatório ($\sum$)
O somatório realiza a adição sequencial dos valores no intervalo de $i$ até $n$:
$$\sum_{k=i}^{n} k = i + (i+1) + \dots + n$$
* **Lógica:** A variável acumuladora inicia em `0` e soma o valor corrente de `i` a cada iteração até atingir `n`.

### 2. Produtório ($\prod$)
O produtório realiza a multiplicação sequencial dos valores no intervalo de $i$ até $n$:
$$\prod_{k=i}^{n} k = i \times (i+1) \times \dots \times n$$
* **Lógica:** A variável acumuladora inicia em `1` (elemento neutro da multiplicação) e multiplica o valor corrente de `i` a cada iteração até atingir `n`.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório ou baixe os scripts desejados.
3. Execute o script de somatório ou produtório no terminal:

```bash
# Para o Somatório
python somatorio.py

# Para o Produtório
python produtorio.py
