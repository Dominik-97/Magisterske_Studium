# Správa obchodní korporace v úpadku

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

OR use proper Markdown YAML metablock syntax like this:
```yaml
---
Keywords: 
  - no_TOC
  - k1
  - k2
  - k3
  ... etc.
---
```

Makefile will then ignore the `--toc` part of the basic pandoc command, and will only use tha basic command withoud the `--toc` declaration.
