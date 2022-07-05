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
    public ListNode mergeNodes(ListNode head) {
        ListNode dummy = new ListNode();
        ListNode res = dummy;
        ListNode current = head.next;
        int sum = 0;
        while(current != null){
            if(current.val == 0){
                ListNode node = new ListNode(sum);
                dummy.next = node;
                dummy = dummy.next;
                sum = 0;
            }else{
                sum += current.val;
            }
            current = current.next;
        }
        return res.next;
    }
}