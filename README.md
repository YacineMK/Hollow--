# Hollow-ホロウ



### Project setup

1. **Download raylib in python3**

2. **Fork the repository and clone the repository to your local machine:**

   ```shell
   git clone https://github.com/<your_github_username>/Hollow--.git
   ```

3. **installing dependecies**
   1. **Fedora**
      ```shell
      sudo dnf install python3
      ```
      ```shell
      python3 -m pip install raylib
      ```

   3. **Arch**
   for arch users, you have to create a virtual environement in order to able to install packages via `pip` .
      ( if you don't have python installed make sure to run the following )
      ```shell
      sudo pacman -Syu && pacman -S install python
      ```
      ```shell
      python -m virtualenv .venv
      ```
      then simply activate it to be able to use it
      ```shell
      source .venv/bin/activate
      ```
      after that you will be able to run
      ```shell
      python -m pip install raylib
      ```

4. **Run code**

   ```shell
   python3 main.py
   ```


