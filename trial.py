new_str = """
  __ __  __        _ _ _ _ _    _ _ _ _ _               
 |  |  ||  \      |         |  |         |  \      /
 |  |  ||   \     |         |  |         |   \    /  
 |  _  ||_ __\    |__ _ _ _ |  |_ _ _ _ _|    \  /     
 |  |  ||     \   |            |                |
 |  |  ||      \  |            |                |
 |__|__||       \ |            |                |

  _ _ _ _   _ _ _ _    _______    _ _ _ _                _ _ _ _ _     __
 |       |    |       |      /      |       |       |   |         /   |  \        \    /
 |       |    |       |     /       |       |       |   |        /    |   \        \  / 
 |_ _ _ _|    |       |    /        |       |_______|   |       /     |_ _ \        \/
 |       |    |       |   /         |       |       |   |      /      |     \       |
 |       |    |       |   \         |       |       |   |     /       |      \      |
 |____ __|  __|____   |    \        |       |       |   |_ _ /        |       \     |

                                
 --------- ---------     \    / ---------  |       |        *   *     ---------
     |     |       |      \  /  |       |  |       |      *   *   *   | <   > |
     |     |       |       \/   |       |  |       |       *     *    |   |   |
     |     |       |        |   |       |  |       |        *   *     |       |
     |     |       |        |   |       |  |       |         * *      |       |
     |     |_ _ _ _|        |   |_ _ _ _|  |_ _ _ _|          *       |_ _ _ _|


 """
 

def birthday_wish():
    result = input("Is Today Your Birthday ? (Yes,No) ")
    if result == 'Yes':
        print(new_str)


birthday_wish()