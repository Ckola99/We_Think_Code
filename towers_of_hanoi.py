# The hanoi function solves the Towers of Hanoi problem for `n` disks, moving them from the source rod to the target rod 
# using the spare rod as an auxiliary. It recursively moves disks while maintaining the rules of the puzzle.
# please see this youtube video for explanation 

def hanoi(n, source, target, spare, source_name="Source", target_name="Target", spare_name="Spare"):
    if n > 0:
        # Step 1: Move the top (n-1) disks from the source rod to the spare rod,
        # using the target rod as an auxiliary.
        hanoi(n - 1, source, spare, target, source_name, spare_name, target_name)
        
        # Step 2: Move the nth disk (largest disk in the current stack) from the source rod
        # directly to the target rod, following the Towers of Hanoi rules.
        target.append(source.pop())
        
        # Step 3: Move the (n-1) disks from the spare rod to the target rod,
        # using the source rod as an auxiliary.
        hanoi(n - 1, spare, target, source, spare_name, target_name, source_name)

# Initial setup of the rods with disks, where 5 is the largest disk and 1 is the smallest.
source = [5, 4, 3, 2, 1]  # The source rod, initially holding all the disks in descending order.
target = []  # The target rod, which starts empty and will hold all disks at the end.
spare = []   # The spare rod, used as an auxiliary to assist in moving disks.

# Run the hanoi function with 5 disks.
hanoi(len(source), source, target, spare)

# Final state of rods after all disks have been moved to the target rod.
print("\nsource:", source)  # Should be empty after completion.
print("\nFinal target rod:", target)  # Should contain all disks in order.
print("\nspare:", spare)  # Should be empty after completion.
