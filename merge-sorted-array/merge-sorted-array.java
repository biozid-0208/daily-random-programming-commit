class Solution {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    int end = m + n - 1;
    // backward from nums1
    int index1 = m - 1;
    int index2 = n - 1;
    while (index1 >= 0 && index2 >= 0) {
      if (nums1[index1] > nums2[index2]) {
        nums1[end] = nums1[index1];
        index1--;
      } else {
        nums1[end] = nums2[index2];
        index2--;
      }
      end--;
    }

    // left element
    while (index2 >= 0) {
      nums1[index2] = nums2[index2];
      index2--;
    }
  }
}