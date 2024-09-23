{ pkgs ? import <nixpkgs> {} }:

let
  unstable = import (builtins.fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/nixpkgs-unstable.tar.gz";
  }) {};

in pkgs.mkShell {
     buildInputs = [
     pkgs.python3
     pkgs.python3Packages.jupyter
     pkgs.python3Packages.jupyterlab
     pkgs.python3Packages.faiss
     pkgs.python3Packages.requests
     pkgs.python3Packages.numpy
     pkgs.python3Packages.pandas
     pkgs.python3Packages.pillow
     pkgs.python3Packages.matplotlib
     pkgs.python3Packages.seaborn
     pkgs.python3Packages.scipy
     pkgs.python3Packages.ollama
     pkgs.vim
     unstable.ollama-rocm
  ];

  shellHook = ''
    export PYTHONPATH=$PYTHONPATH:${pkgs.python3.sitePackages}
    echo "Starting Ollama..."
    nohup ollama serve &>/dev/null &

    echo "Pulling llava:"
    ollama pull llava
  '';
}
