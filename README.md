# dna-analayzer-by-command-line
## about
dna analayzer is a system that loads, analyzes, manipulates and saves DNA sequences, using cli and design pattern principles. 
## author
Efrat Granit
## general explanation about the design patterns I used

The main defines with the singleton design pattern an one instance class which manages the dna dictionary and contains get and set methods 
Create the access to functions of command with factory design pattern – which get the name of function, after a validation check at the main, and returns suitable reference to class of the wanted method 
With reference to wanted method – the suitable for current command – we gonna define with command design pattern the activation of method.
About the batch command – I used the factory and the batch itself was a regular command with inner implementation similar to the main of cli

# available commands running cli
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
