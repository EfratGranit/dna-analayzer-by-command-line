# dna-analayzer-by-command-line

## general explanation about the design patterns I used

The main defines with the singleton design pattern an one instance class which manages the dna dictionary and contains get and set methods 
Create the access to functions of command with factory design pattern – which get the name of function, after a validation check at the main, and returns suitable reference to class of the wanted method 
With reference to wanted method – the suitable for current command – we gonna define with command design pattern the activation of method.
About the batch command – I used the factory and the batch itself was a regular command with inner implementation similar to the main of cli


## function expected input and output

### note: for all commands, if the input is invalid,  error message is printed, but cli never fall

●[argument] - Words starting with "[", ending with "]" represent optional
arguments.
● <argument> - Words starting with "<", ending with ">" represent required
arguments.
● arg1|arg2 - Pipe sign ("|") between words represents that each one of them can
be used.

"#my_id" means sequence with id number my_id
@short-seq refers to the sequence named short-seq

all of creation commands expects to get new name of sequence, else - prints error message and do nothing
if default name is used - the command_manage will find name which doesnt exist and use it - should not fall at such a case
## creation commands
### new 
generate and save new dna sequence with given detailes
### load  
generate and save dna sequence from exist file
### dup 
duplicate exist dna seqeunce into new sequence
## management commands
### save
save the exist sequence to file
### del
delete the exist sequnce from the system
## manipulation commands
### replace
replace chars at given indexes to another chars
### slice
slices exist sequence 
## sequence commands
### find
return first index on which substring exist in the sequence
### findAll
return all indexes on which substring exist in the sequence
### len
return length of exist sequence
## batch commands
the batch is a manageable performance of the cli, which gets the commands in infinite loop and keeps them, for running with the command run.
### batch
creates new batch 
### batchlist 
prints all of commands of the batch
### run
run all of command at the batch in loop
