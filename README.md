# 2024-Ingenium
Repo per il corso facoltativo Ingenium 2023/2024



# LaTeX
`sudo apt update`

`sudo apt install texlive texlive-latex-extra texlive-science texlive-lang-italian`

Se necessario : `sudo apt install latexmk`


```
{
    "[python]": {
        "editor.formatOnType": true
    },

"latex-workshop.latex.outDir": "%DIR%/tmp",

"latex-workshop.latex.recipes": [
    {
      "name": "pdflatex-1",
      "tools": [
        "pdflatex",
        "copypdf",
      ]
    }
],

"latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-output-directory=%OUTDIR%",
        "--shell-escape",
        "%DOC%"
      ],
      "env": {}
    },
    {
        "name": "copypdf",
        "command": "cp",
        "args": [
          "%OUTDIR_W32%/%DOCFILE%.pdf",
          "%DIR_W32%/"
        ]
      },
],
"latex-workshop.latex.autoBuild.run": "never",
"git.confirmSync": false

}



```

