#include <linux/highmem.h>
#include <linux/version.h>
#include <linux/module.h>
#include <linux/unistd.h>

static unsigned long *sys_call_table;
unsigned long * orig_saved;


int make_rw(unsigned long address)  
{  
        unsigned int level;  
        pte_t *pte = lookup_address(address, &level);//查找虚拟地址所在的页表地址  
        if (pte->pte & ~_PAGE_RW)  //设置页表读写属性
                pte->pte |=  _PAGE_RW;  
          
        return 0;  
}  
  
  
  
int make_ro(unsigned long address)  
{  
        unsigned int level;  
        pte_t *pte = lookup_address(address, &level);  
        pte->pte &= ~_PAGE_RW;  //设置只读属性
  
        return 0;  
} 

asmlinkage long sys_mycall(void)
{
    printk(KERN_ALERT "i am hack syscall!\n");
    return 0;
}

static int syscall_init_module(void)  
{  
		sys_call_table = (unsigned long *) simple_strtoul("ffffffff81801400",NULL,16);
        printk(KERN_ALERT "sys_call_table: 0x%p\n", sys_call_table);//获取系统调用表的地址
		
        orig_saved = (unsigned long *)(sys_call_table[223]);  //保存原有的223号的系统调用表的地址
        printk(KERN_ALERT "orig_saved : 0x%p\n", orig_saved );  
  
        make_rw((unsigned long)sys_call_table);  //修改页的写属性
        sys_call_table[223] = (unsigned long *)sys_mycall;  //将223号指向自己写的调用函数
        make_ro((unsigned long)sys_call_table);  
  
        return 0;  
}

static void syscall_cleanup_module(void)  
{  
        printk(KERN_ALERT "Module syscall unloaded.\n");  
  
        make_rw((unsigned long)sys_call_table);  
        sys_call_table[223] = (unsigned long *) orig_saved ;   
        make_ro((unsigned long)sys_call_table);  
}

module_init(syscall_init_module);  
module_exit(syscall_cleanup_module);  
  
MODULE_LICENSE("GPL");  
MODULE_DESCRIPTION("mysyscall"); 
