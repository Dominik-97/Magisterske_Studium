If you do not want to include TOC in the resulting file, you can just add `no_TOC` to the Keywords keyword in the yaml metadata block.

```yaml
---
Keywords: no_TOC
---
```

OR

```yaml
---
Keywords: [no_TOC, other keywords ..., ...]
---
```

Makefile will then ignore the `--toc` part of the basic pandoc command, and will only use tha basic command withoud the `--toc` declaration.
