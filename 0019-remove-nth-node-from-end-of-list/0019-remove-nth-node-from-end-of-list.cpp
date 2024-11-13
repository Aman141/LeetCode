/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* head1 = head;
        ListNode* head2 = head;
        int count = 0;
        while(head2!= NULL) {
            count++;
            head2 = head2->next;
    }
        cout<<count;
        if(count == 1) {
            head = NULL;
            return head;
        }
        if(count == n) {
            head = head->next;
            return head;
        }
        
        int front = count-n;
        while(front>1){
            head1 = head1->next;
            front --;
        }
        ListNode *next = head1->next->next;
        head1->next = next;
        
        
        

        
        return head;
    }
};