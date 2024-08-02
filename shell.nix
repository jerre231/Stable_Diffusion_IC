{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
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
    pkgs.vim
  ];

  shellHook = ''
  '';
}
