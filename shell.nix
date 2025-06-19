with import <nixpkgs> {};
pkgs.mkShell {
  nativeBuildInputs = with pkgs.buildPackages; [
    python312
    uv
  ];
}
