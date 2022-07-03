start_options = [{'selector': '1', 'prompt': 'The campsite! ', 'return': '1'},
                 {'selector': '2', 'prompt': 'The middle of the woods!', 'return': '2'}]

start = '“Ahh, here we are.” Samuel stepped out of the car and took a deep breath.\n' \
        ' The smells of the pines filled the air as wind swept down off the mountains. “The Woods of Darkness.”\n' \
        '“I still don’t get why it’s called the ‘Woods of Darkness.’” Livia climbed out of the passenger’s seat,\n' \
        ' then walked around to the trunk, where she began to unload the camping supplies.\n' \
        '“There’s nothing that dark about it. It’s just an ordinary patch of woods.”\n' \
        '“An ordinary patch of woods home to the most fearsome monster the world has ever seen!” Samuel grinned.\n' \
        '“My grandpa told me all about it! It has horns, and thick wool filled with tree branches, leaves, and the bones of its victims!”\n' \
        '“You grandpa tells you all sorts of things.” Livia sighed and slung a backpack over her shoulders.\n' \
        '“In any case, we’re here. You drug me out. Whoopee. Now, where are we camping?\n'

part_A = '“Oh, we’re camping in the campsite.” \n' \
         'Samuel started walking out of the parking lot toward the marked location for tents and campfires. \n' \
         '“After all, that’s where a monster is most likely to attack!”\n' \
         'Livia rolled her eyes, but followed Samuel. Soon, they had their tents pitched in the small clearing.\n' \
         'Pine trees rose tall on all sides, and Samuel sighed as he took it all in.\n' \
         'Night was coming on fast, and soon, they had a roaring campfire in between their two tents, and sat around the flames roasting marshmallows.\n' \
         'As they did, though, a scream echoed through the air, coming from deeper into the woods.\n' \
         'Samuel jumped to his feet, a smile spreading across his face.\n'

A_options = [{'selector': '1', 'prompt': 'Go investigate! ', 'return': '1'},
             {'selector': '2', 'prompt': 'Bunker down in the tent!', 'return': '2'},
             {'selector': '3', 'prompt': 'Make a monster trap!', 'return': '3'}]

part_B = '“We’re going straight to the center of the woods!” Samuel declared loudly.\n' \
         '“That’s the place we’re most likely to see the monster just wandering through the woods!”\n' \
         '“And if we get in trouble for camping in a non-designated area?”\n' \
         '“Just part of the experience!” Samuel struck off into the woods, with Livia following closely behind.\n' \
         'It took the two of them the better part of half an hour to find a suitable clearing, where the trees parted just enough for them to pitch their two tents.\n' \
         'As the night began to fall about them, they sat down and began to eat their marshmallows cold, as they didn’t want to risk a fire.\n' \
         'Suddenly, though, a scream echoed through the air, coming from only a short distance away from their tent.\n' \
         'Samuel leapt to his feet, a smile spreading across his face.\n'

B_options = [{'selector': '1', 'prompt': 'Go investigate! ', 'return': '1'},
             {'selector': '2', 'prompt': 'Bunker down in the tent!', 'return': '2'},
             {'selector': '3', 'prompt': 'Make a monster trap!', 'return': '3'}]

part_C = '“Come on!” Samuel raced off into the woods, leaving the comfort of the campsite behind.\n' \
         'Samantha followed closely, her breathing ragged as she raced through the woods.\n' \
         'In the darkness, they tripped over fallen logs, sprawled across gnarled tree roots, and fell headlong into puddles of mud.\n' \
         'Up ahead, a dark form could be seen thrashing amidst the trees, and Samuel felt a smile growing across his face.\n' \
         'He grabbed a flashlight off his belt, pointed it forward, and flicked the switch on.\n' \
         'To his immense surprise, he found a rather hairy creature with the lower body of a sheep and the upper body of a man.\n' \
         'To his even greater surprise, the creature was dangling upside-down from a snare, and kicked and screamed wildly.\n' \
         '“Get me down!” It called out loudly. “I don’t want to be eaten!”\n'

C_options = [{'selector': '1', 'prompt': 'Cut the thing down', 'return': '1'},
             {'selector': '2', 'prompt': 'Leave it to dangle', 'return': '2'}]

part_D = '“Inside the tent!” Samuel ordered, his bravery evaporating quicker than a drop of water on hot cement.\n' \
         'He dove back inside his own tent, and was somehow unsurprised when Livia joined him.\n' \
         'They zipped the tent shut, and tried not to think about the fact that they were only separated from the monster\n' \
         'by a piece of fabric that could be knocked over by a strong wind.\n' \
         'Outside, the screaming only grew louder. Footsteps echoed, followed by the shouts of men with loud, thundering voices.\n' \
         '“Get hold of it!”\n' \
         '“There! Watch the hooves!”\n' \
         '“I’ve got the bag!”\n' \
         'The screams reached a fever pitch, and Samuel tentatively unzipped the tent and poked his head out.\n' \
         'There was a loud crash, and something streaked past.\n' \
         'He couldn’t be certain, but until his dying day, he couldn’t escape the image of a freshly-sheared,\n' \
         'half-human, half-sheep racing through the woods, followed soon-after by three poachers each carrying a bag of wool over their shoulders.\n'

part_E = '“Quick!” Samuel grabbed the bag of marshmallows, stuck several of them on sticks, and unzipped his tent. “Help me!”\n' \
         'Livia, for her part, simply dove into her own tent and waited. Samuel quickly set out a number of the tasty treats, then dove into Livia’s tent and zipped it up.\n' \
         'They clutched each other as the screams grew louder, and a number of voices began to echo through the woods.\n' \
         '“Get hold of it!”\n' \
         '“There! Watch the hooves!”\n' \
         '“I’ve got the bag!”\n' \
         'The screams reached a fever pitch, then suddenly cut off. There was a scramble of hooves through the campsite, followed by a munching sound.\n' \
         ' Samuel felt a grin break across his face, and he unzipped the tent and jumped out.\n' \
         '“AHHHH!” The scream pierced the air again as something moved within Samuel’s tent. The creature quickly zipped himself into the tent, hiding him from Samuel’s sight.\n' \
         ' From that moment on, though he only caught a glimpse of the creature, he was never quite able to escape the image of a freshly-sheared,\n' \
         'half-human, half-sheep creature that had just been caught in the act of stealing a marshmallow.\n' \
         'Samuel blinked, then looked up as three poachers walked through the woods, each carrying a bag of wool over their shoulders.\n' \
         'He slipped back into the tent with Livia, said not a word, and gave a simple nod.\n' \
         'Working by the light of the moon, they soon packed up Livia’s tent and left, allowing the strange monster to remain in the privacy of Samuel’s tent for the rest of the night.\n'

part_F = '“Oh, thank you!” The monster gasped as Samuel pulled out a pocketknife and cut him down. “Thank you thank you thank you! Now run, before they catch you, too!”\n' \
         'The monster turned and bounded into the woods, making it three steps before he stepped into a second snare.\n' \
         'There was a sharp twang, and with a rush of wind and leaves, the sheep-man was slung up into the air once more.\n' \
         'His head smacked against the trunk of the tree, and he slumped, unconscious.\n' \
         'More footsteps began to echo from deeper in the woods, and Samuel glanced at Livia.\n' \
         'He quickly cut the sheep-man down once again, then drug him into a patch of nearby brush.\n' \
         'With that, they turned and ran, fleeing desperately back down toward their car.\n' \
         'After all… If a monster was scared of something, what would the two of them be able to do against it?\n'

part_G = '“No, I think I’ll leave you up there.” Samuel shook his head. “I don’t know why you’re up there, but I’m sure you deserve it.”\n' \
         'Suddenly, from deeper in the woods, footsteps began to echo.\n' \
         'The monster howled louder, and a moment later, three men wielding enormous shears and canvas bags came tromping out of the trees.\n' \
         'They looked at the two teenagers, and one of them coughed. “Just what are you kids doing here?”\n' \
         '“We’re… Ahh… What are you doing here?” Samuel countered.\n' \
         '“We’re with the Monster Management Agency.” The leaner shrugged. “It’s our job to catch and shear this guy ever year, and dehorn him if necessary."\n' \
         '"Keeps him from getting all wooly and scary, which, of course, cuts down on the number of reported monster sightings,\n' \
         'the number of people who get lost in the woods trying to run away from him, and so on."\n' \
         '"We’ll only be a few moments, you two can run along.”\n' \
         'Samuel and Livia watched, unable to believe what they were seeing, as the three men set upon the monster, and soon enough had him sheared.\n' \
         'They then cut him down, and he dashed away in shame.\n' \
         'With that, the three agents left, and Samuel and Livia were left standing in the woods.\n' \
         'It was a story that Samuel would never be able to get out of his head… Even if he didn’t even believe it himself at that time.'
