my shellcode
============

shellcode is in the shellcode directory.  the higherarchy is:

```
shellcode
	[arch]
		[os]
			[optimization strategy]
				src/      assembly and python source
				obj/      object files of source
				elf/      assembled elfs
				bin/      .text segment of elfs
				py/       python code of string containing .text segment
				tests/    python tests
				testing/  programs and scripts to run tests
```
