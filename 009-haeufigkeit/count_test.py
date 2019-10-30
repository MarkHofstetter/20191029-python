import pytest
import count

def test_count_occurences():      
    data = [
        [[3,4,5,3,4,3], { 3:3, 4:2, 5:1 }],
        [[3,4,5,2,3,4,3], { 2:1, 3:3, 4:2, 5:1 }]
        ]        
        
    for i in data:    
        stat = count.count_occurences(i[0])        
        assert stat == i[1]
    
def test_count_occurences2():      
    data = [
        [[3,4,5,3,4,3], { 3:3, 4:2, 5:1 }],
        [[3,4,5,2,3,4,3], { 2:1, 3:3, 4:2, 5:1 }]
        ]        
        
    for i in data:    
        stat = count.count_occurences(i[0])        
        assert stat == i[1]
    
