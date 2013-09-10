import static org.junit.Assert.*; 
import org.junit.Test;

public class GiaiPTB1Test 
{ 
    @Test 
    public void Test1()
    { 
        GiaiPT pt = new GiaiPT(); 
        int result = pt.GiaiPTB1(1, 1);
        assertEquals(result, -1);
    } 

    @Test 
    public void Test2()
    {
    	GiaiPT pt = new GiaiPT();
    	int result = pt.GiaiPTB1(10, -90)
    	assertEquals(result, 9);
    }
}