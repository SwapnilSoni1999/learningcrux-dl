# learningcrux-dl

A utility to download courses/videos from learningcrux.com by using [Youtube-DL](https://github.com/ytdl-org/youtube-dl)

<hr>

## How to use

install from pypi.org

```sh
$ sudo pip install learningcrux-dl
```

<hr>

## Instructions

The tool can be accesed via `lcx-dl` command.
eg.
```sh
$ lcx-dl --url https://www.learningcrux.com/course/some-course
```
> Make sure you provide `--url` or `-u` which is required.

and it will download the whole course.

You can also provide `--output <your-path-here>` to save on your desired directory.

eg.
```sh
$ lcx-dl --url https://www.learningcrux.com/course/some-course --output ~/udemy
```

and it will save in the given path.

## Command Docs
| Flag | Usage | 
| ------ | ------ | 
| -u <br> --url | url of course/video from learningcrux |
| -o <br> --output | Output path |


### Limitations
- Cannot resume download. (will be fixed in future updates)
- Cannot download single video. (Releasing ASAP)
- Uses youtube-dl so downloading can be done sequencially (no multithreads for now)
- You must use `--output` arg to make the downloader work.

#### License
- SwapnilSoni1999 (Unlicensed)

<h4>Huge thanks to all <a href="https://github.com/SwapnilSoni1999/learningcrux-dl/graphs/contributors">Contributors</a></h4>
