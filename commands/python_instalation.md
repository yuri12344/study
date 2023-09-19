# Instalação do Python com ASDF

Siga os passos abaixo para instalar o Python usando o ASDF:

1. Atualize os pacotes existentes:

   ```bash
   sudo apt-get update
   ```

2. Instale dependencias necessarias

   ```bash
   sudo apt-get install git --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
   ```

3. Clone o repositorio ASDF

   ```bash
   git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.10.2
   ```

4. Adicione o ASDF ao .bashrc

   ```bash
   echo ". $HOME/.asdf/asdf.sh" >> ~/.bashrc
   ```

5. Atualize o terminal

   ```bash
   source .bashrc
   ```

6. Adicione o plugin Python ao ASDF

   ```bash
   asdf plugin-add python
   ```

7. Liste todos os pythons

   ```bash
   asdf list all python  > text.txt & nano text.txt
   ```

8. Install the desired version

   ```bash
   asdf install python 3.11.5
   ```

9. Set the global python
   ```bash
   asdf global python 3.11.5
   ```
