# html2pdf

Tool to download a webpage as PDF when you need to do it programmatically.


## Even simpler method

This works but as far as I know you cannot easily remove the header and footer:
```bash
$ google-chrome-stable --headless --disable-gpu --print-to-pdf="output.pdf" "https://example.org"
```


## Requirements

- You need an installation of [Apptainer](https://apptainer.org/) (e.g. following
  the [quick
  installation](https://apptainer.org/docs/user/latest/quick_start.html#quick-installation)).
  Alternatively, [SingularityCE](https://sylabs.io/singularity/) should also
  work.


## How to use it

First download the container image (ending with *.sif) from here:
https://github.com/bast/html2pdf/releases

Make the image executable and then (A4 is the default paper size):
```bash
$ ./html2pdf.sif --url=https://example.org --pdf=output.pdf
```

Or if you prefer the Letter paper size:
```bash
$ ./html2pdf.sif --url=https://example.org --pdf=output.pdf --size=Letter
```


## About the container image

To build the image, I have used [this wonderful
guide](https://github.com/singularityhub/singularity-deploy) as starting point
and inspiration.

I find it important that everybody can verify how the container image was
built. And you can! You can inspect the definition file and all scripts which
are all part of this repository.
