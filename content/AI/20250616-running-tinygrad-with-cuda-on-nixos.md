Title: Running tinygrad with CUDA on NixOS
Date: 2025-06-16 08:40
Tags: AI

I started to play around with NixOS a few weeks ago and until now I am quite happy with it. I installed it on an older
PC with a Geforce GT 1030 and wanted to see if I get tinygrad running with the CUDA back-end on it. I learned about
nix-shell and, after a while, was able to set up such a shell that supports tinygrad on CUDA. I was not able to find
examples that worked directly for my use case, so I will post that here, for future reference. The main customizations
for me where:

- Adding clang as the shell compiler
- LD_LIBRARY_PATH needs `${pkgs.cudatoolkit}/lib` for `libnvrtc.so`
- I added `NIX_ENFORCE_NO_NATIVE=0` so that tinygrad can pass `-march=native` to clang

Here is my complete nix-shell:

```
with import <nixpkgs> {};
clangStdenv.mkDerivation {
  name = "clang-nix-shell";
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = with pkgs.buildPackages; [
    python312
    uv
  ];
  buildInputs = with pkgs; [
    git gitRepo gnupg autoconf curl
    procps gnumake util-linux m4 gperf unzip
    cudatoolkit linuxPackages.nvidia_x11
    libGLU libGL
    xorg.libXi xorg.libXmu freeglut
    xorg.libXext xorg.libX11 xorg.libXv xorg.libXrandr zlib
    ncurses5 stdenv.cc binutils
  ];
  shellHook = ''
    export CUDA_PATH=${pkgs.cudatoolkit}
    export LD_LIBRARY_PATH=${pkgs.linuxPackages.nvidia_x11}/lib:${pkgs.ncurses5}/lib:${pkgs.cudatoolkit}/lib
    export EXTRA_LDFLAGS="-L/lib -L${pkgs.linuxPackages.nvidia_x11}/lib"
    export EXTRA_CCFLAGS="-I/usr/include"
    NIX_ENFORCE_NO_NATIVE=0
  '';
}
```

You might also need to remove the `--target` argument to clang from the tinygrad `runtime/ops_cpu.py`. It gave me
warning, but I am not sure if it actually [breaks things](https://github.com/NixOS/nixpkgs/pull/323869):

```
14c14
<     args = ['-march=native', f'--target={target}-none-unknown-elf', '-O2', '-fPIC', '-ffreestanding', '-fno-math-errno', '-nostdlib', '-fno-ident']
---
>     args = ['-march=native', '-O2', '-fPIC', '-ffreestanding', '-fno-math-errno', '-nostdlib', '-fno-ident']
```
