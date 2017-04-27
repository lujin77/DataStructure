package sort;

import java.util.Arrays;

/**
 * 快速排序的Java实现
 *
 * @Author: lujin
 * @Created Date: 2016/8/23 9:23
 * @Version 1.0.0
 * @LastModify 2016/8/23 9:23
 */
public class QuickSort {

    /**
     * 原地进行快速排序
     */
    public static <T extends Comparable> void sort(T[] array) {
        // 入参检查
        if (array == null || array.length == 0) {
            System.out.println("[WARNING] input array to sort is null or emtpy, do nothing as default");
            return;
        }
        //构造标志变量
        int low = 0;
        int high = array.length - 1;
        qsort(array, low, high);
    }

    /**
     * 递归形式快速排序
     *
     * @param arr  待排序数组
     * @param low  排序的数组下界
     * @param high 排序的数组上界
     */
    public static <T extends Comparable> void qsort(T[] arr, int low, int high) {

        if (low >= high) return;

        //递归划分
        int pivot = partition(arr, low, high);
        qsort(arr, low, pivot - 1);
        qsort(arr, pivot + 1, high);

    }

    /**
     * 按照指定的上下界计算出中轴，中轴满足：左边的元素都小于它，右边的元素都大于它
     *
     * @param arr  待计算的数组
     * @param low  参与计算的数组下界
     * @param high 参与计算的数组上界
     * @return 满足要求的中轴元素
     */
    public static <T extends Comparable> int partition(T[] arr, int low, int high) {

        //设置最小值为轴
        T pivot = arr[low];

        int i = low, j = high;
        while (i < j) {
            // 找到右边第比轴小的值
            while (j > i && arr[j].compareTo(pivot) >= 0) --j;
            // 找到左边第比轴大的值
            while (i < j && arr[i].compareTo(pivot) <= 0) ++i;
            // 交互2个值
            if (i < j) {
                T tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
        //最终将轴归位
        arr[low] = arr[i];
        arr[i] = pivot;

        return i;
    }
}
