/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slowPtr = head, fastPtr = head;
        int counter = 0;
        
        while(fastPtr  != null){
            counter++;
            fastPtr = fastPtr.next;
        }
        counter = counter/2;
        while(counter > 0){
            counter--;
            slowPtr = slowPtr.next;
        }
        return slowPtr; 
        
    }
}