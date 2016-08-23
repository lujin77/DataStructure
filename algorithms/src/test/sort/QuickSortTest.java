package sort;

import org.junit.Test;

import java.util.Arrays;

/**
 * QuickSort Tester.
 *
 * @Author: lujin
 * @Created Date: 2016/8/23 9:49
 * @Version 1.0.0
 * @LastModify 2016/8/23 9:49
 */
public class QuickSortTest {


    @Test
    public void testSort() throws Exception {
        Integer[] arr = {2, 5, 1, 4, 0, 6, 4};
        System.out.println("[INFO] befor: " + Arrays.toString(arr));
        QuickSort.sort(arr);
        System.out.println("[INFO] after: " + Arrays.toString(arr));
    }

} 
