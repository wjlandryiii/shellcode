my shellcode
============

shellcode is in the shellcode directory.  the higherarchy is:

```
shellcode
	[arch]
		[os]
			[optimization stratagy]
				src/ assembly source
				obj/ object files of source
				elf/ assembled elfs
				bin/ .text segment of elfs
				py/  python code of string containing .text segment
```
