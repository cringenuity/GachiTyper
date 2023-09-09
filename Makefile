CompilerPath := "C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe"
WrapperChar = \\u2642\\ufe0f # ♂️
OutputDir := out
SubsListsDir := substitution_lists

SrcFiles := $(wildcard src/*.py)
SubstitutionLists := $(wildcard $(SubsListsDir)/*.txt)

.PHONY: all generate-all compile-all clean

all: generate-all compile-all

generate-all: $(addprefix $(OutputDir)/, $(notdir $(SubstitutionLists:.txt=.ahk)))
compile-all:  $(addprefix $(OutputDir)/, $(notdir $(SubstitutionLists:.txt=.exe)))

clean:
	rm -rf $(OutputDir)

$(OutputDir)/%.ahk: $(SubsListsDir)/%.txt $(SrcFiles)
	py src/Main.py -w $(WrapperChar) -o $@ $<
	touch $@

$(OutputDir)/%.exe: $(OutputDir)/%.ahk
	$(CompilerPath) /in $^ /out $(notdir $@) /silent
	touch $@
