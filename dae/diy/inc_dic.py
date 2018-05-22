#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import os # 操作系统模块
import linecache # 引用缓存读取文件模块

# 构造单元素字典
def dic_make_one(path_p="",split_p="\n"):
    
    dic_p = {}
    str_t = ""
    with open(path_p, 'r', encoding="utf-8") as f:
        str_t = f.read()
    list_t = str_t.split(split_p)
    i = 0
    for x in list_t:
        dic_p[x] = i
        i += 1
    
    return dic_p
    
# 构造单元素字典
def dic_make_one_cache(path_p=""):

    dic_p = {}
    
    try:
    
        cache_data = linecache.getlines(path_p)
        i = 0
        for line in range(len(cache_data)):
            dic_p[cache_data[line].replace("\n","")] = i
            i += 1
    except:
        pass

    return dic_p

#停止词字典
dic_stop ={
"一一":0,
"一下":0,
"一个":0,
"一些":0,
"一何":0,
"一切":0,
"一则":0,
"一则通过":0,
"一天":0,
"一定":0,
"一方面":0,
"一旦":0,
"一时":0,
"一来":0,
"一样":0,
"一次":0,
"一片":0,
"一番":0,
"一直":0,
"一致":0,
"一般":0,
"一起":0,
"一转眼":0,
"一边":0,
"一面":0,
"万一":0,
"三天两头":0,
"三番两次":0,
"三番五次":0,
"上下":0,
"上升":0,
"上去":0,
"上来":0,
"上述":0,
"上面":0,
"下列":0,
"下去":0,
"下来":0,
"下面":0,
"不一":0,
"不下":0,
"不久":0,
"不了":0,
"不亦乐乎":0,
"不仅":0,
"不仅仅":0,
"不仅仅是":0,
"不会":0,
"不但":0,
"不光":0,
"不免":0,
"不再":0,
"不力":0,
"不单":0,
"不变":0,
"不只":0,
"不可":0,
"不可开交":0,
"不可抗拒":0,
"不同":0,
"不外":0,
"不外乎":0,
"不够":0,
"不大":0,
"不如":0,
"不妨":0,
"不定":0,
"不对":0,
"不少":0,
"不尽":0,
"不尽然":0,
"不巧":0,
"不已":0,
"不常":0,
"不得":0,
"不得不":0,
"不得了":0,
"不得已":0,
"不必":0,
"不怎么":0,
"不怕":0,
"不惟":0,
"不成":0,
"不拘":0,
"不择手段":0,
"不敢":0,
"不料":0,
"不断":0,
"不日":0,
"不时":0,
"不是":0,
"不曾":0,
"不止":0,
"不止一次":0,
"不比":0,
"不消":0,
"不满":0,
"不然":0,
"不然的话":0,
"不特":0,
"不独":0,
"不由得":0,
"不知不觉":0,
"不管":0,
"不管怎样":0,
"不经意":0,
"不胜":0,
"不能":0,
"不能不":0,
"不至于":0,
"不若":0,
"不要":0,
"不论":0,
"不起":0,
"不足":0,
"不过":0,
"不迭":0,
"不问":0,
"不限":0,
"与其":0,
"与其说":0,
"与否":0,
"与此同时":0,
"专门":0,
"且不说":0,
"且说":0,
"两者":0,
"严格":0,
"严重":0,
"个人":0,
"个别":0,
"中小":0,
"中间":0,
"丰富":0,
"串行":0,
"临到":0,
"为主":0,
"为了":0,
"为什么":0,
"为什麽":0,
"为何":0,
"为止":0,
"为此":0,
"为着":0,
"主张":0,
"主要":0,
"举凡":0,
"举行":0,
"乃至":0,
"乃至于":0,
"之一":0,
"之前":0,
"之后":0,
"之後":0,
"之所以":0,
"之类":0,
"乌乎":0,
"乘势":0,
"乘机":0,
"乘胜":0,
"乘虚":0,
"乘隙":0,
"也好":0,
"也就是说":0,
"也是":0,
"也罢":0,
"了解":0,
"争取":0,
"二来":0,
"二话不说":0,
"二话没说":0,
"于是":0,
"于是乎":0,
"云云":0,
"云尔":0,
"互相":0,
"交口":0,
"产生":0,
"亲口":0,
"亲手":0,
"亲眼":0,
"亲自":0,
"亲身":0,
"人人":0,
"人们":0,
"人家":0,
"什么":0,
"什么样":0,
"什麽":0,
"仅仅":0,
"今后":0,
"今天":0,
"今年":0,
"今後":0,
"介于":0,
"仍旧":0,
"仍然":0,
"从不":0,
"从严":0,
"从中":0,
"从事":0,
"从今以后":0,
"从优":0,
"从古到今":0,
"从古至今":0,
"从头":0,
"从宽":0,
"从小":0,
"从新":0,
"从无到有":0,
"从早到晚":0,
"从未":0,
"从来":0,
"从此":0,
"从此以后":0,
"从而":0,
"从轻":0,
"从速":0,
"从重":0,
"他人":0,
"他们":0,
"他是":0,
"他的":0,
"代替":0,
"以上":0,
"以下":0,
"以为":0,
"以便":0,
"以免":0,
"以前":0,
"以及":0,
"以后":0,
"以外":0,
"以後":0,
"以故":0,
"以期":0,
"以来":0,
"以至":0,
"以至于":0,
"以致":0,
"任何":0,
"任凭":0,
"任务":0,
"企图":0,
"伙同":0,
"伟大":0,
"传说":0,
"传闻":0,
"似乎":0,
"似的":0,
"但凡":0,
"但愿":0,
"但是":0,
"何乐而不为":0,
"何以":0,
"何况":0,
"何处":0,
"何妨":0,
"何尝":0,
"何必":0,
"何时":0,
"何止":0,
"何苦":0,
"何须":0,
"余外":0,
"作为":0,
"你们":0,
"你是":0,
"你的":0,
"使得":0,
"使用":0,
"例如":0,
"依据":0,
"依照":0,
"依靠":0,
"便于":0,
"促进":0,
"保持":0,
"保管":0,
"保险":0,
"俺们":0,
"倍加":0,
"倍感":0,
"倒不如":0,
"倒不如说":0,
"倒是":0,
"倘使":0,
"倘或":0,
"倘然":0,
"倘若":0,
"借以":0,
"借此":0,
"假使":0,
"假如":0,
"假若":0,
"偏偏":0,
"做到":0,
"偶尔":0,
"偶而":0,
"傥然":0,
"允许":0,
"元／吨":0,
"充其极":0,
"充其量":0,
"充分":0,
"先不先":0,
"先后":0,
"先後":0,
"先生":0,
"光是":0,
"全体":0,
"全力":0,
"全年":0,
"全然":0,
"全身心":0,
"全部":0,
"全都":0,
"全面":0,
"八成":0,
"公然":0,
"共同":0,
"共总":0,
"关于":0,
"其一":0,
"其中":0,
"其二":0,
"其他":0,
"其余":0,
"其后":0,
"其它":0,
"其实":0,
"其次":0,
"具体":0,
"具体地说":0,
"具体来说":0,
"具体说来":0,
"具有":0,
"兼之":0,
"再其次":0,
"再则":0,
"再有":0,
"再次":0,
"再者":0,
"再者说":0,
"再说":0,
"决不":0,
"决定":0,
"决非":0,
"况且":0,
"准备":0,
"凑巧":0,
"凝神":0,
"几乎":0,
"几度":0,
"几时":0,
"几番":0,
"几经":0,
"凡是":0,
"凭借":0,
"出于":0,
"出去":0,
"出来":0,
"出现":0,
"分别":0,
"分头":0,
"分期":0,
"分期分批":0,
"切不可":0,
"切切":0,
"切勿":0,
"切莫":0,
"则甚":0,
"刚好":0,
"刚巧":0,
"刚才":0,
"别人":0,
"别处":0,
"别是":0,
"别的":0,
"别管":0,
"别说":0,
"到了儿":0,
"到处":0,
"到头":0,
"到头来":0,
"到底":0,
"到目前为止":0,
"前后":0,
"前此":0,
"前者":0,
"前进":0,
"前面":0,
"加上":0,
"加之":0,
"加以":0,
"加入":0,
"加强":0,
"动不动":0,
"动辄":0,
"勃然":0,
"匆匆":0,
"十分":0,
"千万":0,
"千万千万":0,
"单单":0,
"单纯":0,
"即令":0,
"即使":0,
"即便":0,
"即刻":0,
"即如":0,
"即将":0,
"即或":0,
"即是说":0,
"即若":0,
"却不":0,
"原来":0,
"又及":0,
"及其":0,
"及时":0,
"及至":0,
"双方":0,
"反之":0,
"反之亦然":0,
"反之则":0,
"反倒":0,
"反倒是":0,
"反应":0,
"反手":0,
"反映":0,
"反而":0,
"反过来":0,
"反过来说":0,
"取得":0,
"取道":0,
"受到":0,
"变成":0,
"古来":0,
"另一个":0,
"另一方面":0,
"另外":0,
"另悉":0,
"另方面":0,
"另行":0,
"只当":0,
"只怕":0,
"只是":0,
"只有":0,
"只消":0,
"只要":0,
"只限":0,
"叫做":0,
"召开":0,
"叮咚":0,
"叮当":0,
"可以":0,
"可好":0,
"可是":0,
"可能":0,
"可见":0,
"各个":0,
"各人":0,
"各位":0,
"各地":0,
"各式":0,
"各种":0,
"各级":0,
"各自":0,
"合理":0,
"同一":0,
"同时":0,
"同样":0,
"后来":0,
"后者":0,
"后面":0,
"向使":0,
"向着":0,
"否则":0,
"吧哒":0,
"呆呆地":0,
"呜呼":0,
"周围":0,
"呵呵":0,
"呼哧":0,
"呼啦":0,
"咱们":0,
"哈哈":0,
"哎呀":0,
"哎哟":0,
"哗啦":0,
"哪个":0,
"哪些":0,
"哪儿":0,
"哪天":0,
"哪年":0,
"哪怕":0,
"哪样":0,
"哪边":0,
"哪里":0,
"哼唷":0,
"唯有":0,
"啊呀":0,
"啊哈":0,
"啊哟":0,
"啪达":0,
"啷当":0,
"喔唷":0,
"嗡嗡":0,
"嘎嘎":0,
"嘎登":0,
"嘿嘿":0,
"因为":0,
"因了":0,
"因此":0,
"因着":0,
"因而":0,
"固然":0,
"在下":0,
"在于":0,
"坚决":0,
"坚持":0,
"基于":0,
"基本":0,
"基本上":0,
"处在":0,
"处处":0,
"处理":0,
"复杂":0,
"多么":0,
"多亏":0,
"多多":0,
"多多少少":0,
"多多益善":0,
"多少":0,
"多年前":0,
"多年来":0,
"多数":0,
"多次":0,
"够瞧的":0,
"大不了":0,
"大举":0,
"大事":0,
"大体":0,
"大体上":0,
"大凡":0,
"大力":0,
"大多":0,
"大多数":0,
"大大":0,
"大家":0,
"大张旗鼓":0,
"大批":0,
"大抵":0,
"大概":0,
"大略":0,
"大约":0,
"大致":0,
"大都":0,
"大量":0,
"大面儿上":0,
"失去":0,
"奋勇":0,
"她们":0,
"她是":0,
"她的":0,
"好在":0,
"好的":0,
"好象":0,
"如上":0,
"如上所述":0,
"如下":0,
"如今":0,
"如何":0,
"如其":0,
"如前所述":0,
"如同":0,
"如常":0,
"如是":0,
"如期":0,
"如果":0,
"如次":0,
"如此":0,
"如此等等":0,
"如若":0,
"始而":0,
"姑且":0,
"存在":0,
"存心":0,
"孰料":0,
"孰知":0,
"宁可":0,
"宁愿":0,
"宁肯":0,
"它们":0,
"它们的":0,
"它是":0,
"它的":0,
"安全":0,
"完全":0,
"完成":0,
"实现":0,
"实际":0,
"宣布":0,
"容易":0,
"密切":0,
"对于":0,
"对应":0,
"对待":0,
"对方":0,
"对比":0,
"将才":0,
"将要":0,
"将近":0,
"少数":0,
"尔后":0,
"尔尔":0,
"尔等":0,
"尚且":0,
"尤其":0,
"就地":0,
"就是":0,
"就是了":0,
"就是说":0,
"就此":0,
"就算":0,
"就要":0,
"尽可能":0,
"尽如人意":0,
"尽心尽力":0,
"尽心竭力":0,
"尽快":0,
"尽早":0,
"尽然":0,
"尽管":0,
"尽管如此":0,
"尽量":0,
"局外":0,
"居然":0,
"届时":0,
"属于":0,
"屡屡":0,
"屡次":0,
"屡次三番":0,
"岂但":0,
"岂止":0,
"岂非":0,
"川流不息":0,
"左右":0,
"巨大":0,
"巩固":0,
"差一点":0,
"差不多":0,
"已矣":0,
"已经":0,
"巴巴":0,
"帮助":0,
"常常":0,
"常言说":0,
"常言说得好":0,
"常言道":0,
"平素":0,
"年复一年":0,
"并不":0,
"并不是":0,
"并且":0,
"并排":0,
"并无":0,
"并没":0,
"并没有":0,
"并肩":0,
"并非":0,
"广大":0,
"广泛":0,
"应当":0,
"应用":0,
"应该":0,
"庶乎":0,
"庶几":0,
"开外":0,
"开始":0,
"开展":0,
"引起":0,
"弹指之间":0,
"强烈":0,
"强调":0,
"归根到底":0,
"归根结底":0,
"归齐":0,
"当下":0,
"当中":0,
"当儿":0,
"当前":0,
"当即":0,
"当口儿":0,
"当地":0,
"当场":0,
"当头":0,
"当庭":0,
"当时":0,
"当然":0,
"当真":0,
"当着":0,
"形成":0,
"彻夜":0,
"彻底":0,
"彼时":0,
"彼此":0,
"往往":0,
"待到":0,
"很多":0,
"很少":0,
"後来":0,
"後面":0,
"得了":0,
"得出":0,
"得到":0,
"得天独厚":0,
"得起":0,
"心里":0,
"必定":0,
"必将":0,
"必然":0,
"必要":0,
"必须":0,
"快要":0,
"忽地":0,
"忽然":0,
"怎么":0,
"怎么办":0,
"怎么样":0,
"怎奈":0,
"怎样":0,
"怎麽":0,
"急匆匆":0,
"怪不得":0,
"总之":0,
"总是":0,
"总的来看":0,
"总的来说":0,
"总的说来":0,
"总结":0,
"总而言之":0,
"恍然":0,
"恐怕":0,
"恰似":0,
"恰好":0,
"恰如":0,
"恰巧":0,
"恰恰":0,
"恰恰相反":0,
"恰逢":0,
"您好":0,
"您们":0,
"您是":0,
"惟其":0,
"惯常":0,
"意思":0,
"愤然":0,
"愿意":0,
"慢说":0,
"成为":0,
"成年":0,
"成年累月":0,
"成心":0,
"我们":0,
"我是":0,
"我的":0,
"或则":0,
"或多或少":0,
"或是":0,
"或曰":0,
"或者":0,
"或许":0,
"战斗":0,
"截然":0,
"截至":0,
"所以":0,
"所在":0,
"所幸":0,
"所有":0,
"所谓":0,
"才能":0,
"扑通":0,
"打从":0,
"打开天窗说亮话":0,
"扩大":0,
"抑或":0,
"抽冷子":0,
"拦腰":0,
"按时":0,
"按期":0,
"按照":0,
"按理":0,
"按说":0,
"挨个":0,
"挨家挨户":0,
"挨次":0,
"挨着":0,
"挨门挨户":0,
"挨门逐户":0,
"换句话说":0,
"换言之":0,
"据实":0,
"据悉":0,
"据我所知":0,
"据此":0,
"据称":0,
"据说":0,
"掌握":0,
"接下来":0,
"接着":0,
"接著":0,
"接连不断":0,
"放量":0,
"故意":0,
"故此":0,
"故而":0,
"敞开儿":0,
"敢于":0,
"敢情":0,
"整个":0,
"断然":0,
"方便":0,
"方才":0,
"方能":0,
"方面":0,
"旁人":0,
"无宁":0,
"无法":0,
"无论":0,
"既…又":0,
"既往":0,
"既是":0,
"既然":0,
"日复一日":0,
"日渐":0,
"日益":0,
"日臻":0,
"日见":0,
"时候":0,
"昂然":0,
"明显":0,
"明确":0,
"是不是":0,
"是以":0,
"是否":0,
"是的":0,
"显然":0,
"显著":0,
"普通":0,
"普遍":0,
"暗中":0,
"暗地里":0,
"暗自":0,
"更为":0,
"更加":0,
"更进一步":0,
"曾经":0,
"替代":0,
"最后":0,
"最大":0,
"最好":0,
"最後":0,
"最近":0,
"最高":0,
"有些":0,
"有关":0,
"有利":0,
"有力":0,
"有及":0,
"有所":0,
"有效":0,
"有时":0,
"有点":0,
"有的":0,
"有的是":0,
"有着":0,
"有著":0,
"朝着":0,
"末##末":0,
"本人":0,
"本地":0,
"本着":0,
"本身":0,
"权时":0,
"来不及":0,
"来得及":0,
"来看":0,
"来着":0,
"来自":0,
"来讲":0,
"来说":0,
"极为":0,
"极了":0,
"极其":0,
"极力":0,
"极大":0,
"极度":0,
"极端":0,
"构成":0,
"果然":0,
"果真":0,
"某个":0,
"某些":0,
"某某":0,
"根据":0,
"根本":0,
"格外":0,
"次第":0,
"欢迎":0,
"正值":0,
"正在":0,
"正如":0,
"正巧":0,
"正常":0,
"正是":0,
"此中":0,
"此后":0,
"此地":0,
"此处":0,
"此外":0,
"此时":0,
"此次":0,
"此间":0,
"毋宁":0,
"每个":0,
"每天":0,
"每年":0,
"每当":0,
"每时每刻":0,
"每每":0,
"每逢":0,
"比及":0,
"比如":0,
"比如说":0,
"比方":0,
"比照":0,
"比起":0,
"比较":0,
"毕竟":0,
"毫不":0,
"毫无":0,
"毫无例外":0,
"毫无保留地":0,
"沙沙":0,
"没奈何":0,
"没有":0,
"沿着":0,
"注意":0,
"深入":0,
"清楚":0,
"满足":0,
"漫说":0,
"然则":0,
"然后":0,
"然後":0,
"然而":0,
"照着":0,
"牢牢":0,
"特别是":0,
"特殊":0,
"特点":0,
"犹且":0,
"犹自":0,
"独自":0,
"猛然":0,
"猛然间":0,
"率尔":0,
"率然":0,
"现代":0,
"现在":0,
"理应":0,
"理当":0,
"理该":0,
"瑟瑟":0,
"甚且":0,
"甚么":0,
"甚或":0,
"甚而":0,
"甚至":0,
"甚至于":0,
"用来":0,
"由于":0,
"由是":0,
"由此":0,
"由此可见":0,
"略为":0,
"略加":0,
"略微":0,
"白白":0,
"的确":0,
"的话":0,
"皆可":0,
"目前":0,
"直到":0,
"直接":0,
"相似":0,
"相信":0,
"相反":0,
"相同":0,
"相对":0,
"相对而言":0,
"相应":0,
"相当":0,
"相等":0,
"省得":0,
"看上去":0,
"看出":0,
"看到":0,
"看来":0,
"看样子":0,
"看看":0,
"看见":0,
"看起来":0,
"真是":0,
"真正":0,
"眨眼":0,
"着呢":0,
"矣乎":0,
"矣哉":0,
"知道":0,
"确定":0,
"碰巧":0,
"积极":0,
"移动":0,
"究竟":0,
"穷年累月":0,
"突出":0,
"突然":0,
"立刻":0,
"立即":0,
"立地":0,
"立时":0,
"立马":0,
"竟然":0,
"竟而":0,
"第二":0,
"等到":0,
"等等":0,
"策略地":0,
"简直":0,
"简而言之":0,
"简言之":0,
"类如":0,
"精光":0,
"紧接着":0,
"累年":0,
"累次":0,
"纯粹":0,
"纵令":0,
"纵使":0,
"纵然":0,
"练习":0,
"组成":0,
"经常":0,
"经过":0,
"结合":0,
"结果":0,
"绝不":0,
"绝对":0,
"绝非":0,
"绝顶":0,
"继之":0,
"继后":0,
"继续":0,
"继而":0,
"维持":0,
"综上所述":0,
"缕缕":0,
"罢了":0,
"老大":0,
"老是":0,
"老老实实":0,
"考虑":0,
"而且":0,
"而况":0,
"而又":0,
"而后":0,
"而外":0,
"而已":0,
"而是":0,
"而言":0,
"而论":0,
"联系":0,
"联袂":0,
"背地里":0,
"背靠背":0,
"能否":0,
"能够":0,
"自个儿":0,
"自从":0,
"自各儿":0,
"自后":0,
"自家":0,
"自己":0,
"自打":0,
"自身":0,
"至于":0,
"至今":0,
"至若":0,
"般的":0,
"良好":0,
"若夫":0,
"若是":0,
"若果":0,
"若果":0,
"若非":0,
"范围":0,
"莫不":0,
"莫不然":0,
"莫如":0,
"莫若":0,
"莫非":0,
"获得":0,
"藉以":0,
"虽则":0,
"虽然":0,
"虽说":0,
"行为":0,
"行动":0,
"表明":0,
"表示":0,
"要不":0,
"要不是":0,
"要不然":0,
"要么":0,
"要是":0,
"要求":0,
"规定":0,
"觉得":0,
"譬喻":0,
"譬如":0,
"认为":0,
"认真":0,
"认识":0,
"许多":0,
"论说":0,
"设使":0,
"设或":0,
"设若":0,
"诚如":0,
"诚然":0,
"话说":0,
"该当":0,
"说明":0,
"说来":0,
"说说":0,
"请问":0,
"请勿":0,
"诸位":0,
"诸如":0,
"谁人":0,
"谁料":0,
"谁知":0,
"豁然":0,
"贼死":0,
"赖以":0,
"赶快":0,
"赶早不赶晚":0,
"起先":0,
"起初":0,
"起头":0,
"起来":0,
"起见":0,
"起首":0,
"趁便":0,
"趁势":0,
"趁早":0,
"趁机":0,
"趁热":0,
"趁着":0,
"越是":0,
"转动":0,
"转变":0,
"转贴":0,
"轰然":0,
"较为":0,
"较之":0,
"较比":0,
"达到":0,
"达旦":0,
"迅速":0,
"过于":0,
"过去":0,
"过来":0,
"运用":0,
"近几年来":0,
"近年来":0,
"近来":0,
"还是":0,
"还有":0,
"还要":0,
"这一来":0,
"这个":0,
"这么":0,
"这么些":0,
"这么样":0,
"这么点儿":0,
"这些":0,
"这会儿":0,
"这儿":0,
"这就是说":0,
"这时":0,
"这样":0,
"这次":0,
"这点":0,
"这种":0,
"这般":0,
"这边":0,
"这里":0,
"这麽":0,
"进入":0,
"进去":0,
"进来":0,
"进步":0,
"进而":0,
"进行":0,
"连同":0,
"连声":0,
"连日":0,
"连日来":0,
"连袂":0,
"连连":0,
"迟早":0,
"迫于":0,
"适应":0,
"适当":0,
"适用":0,
"逐步":0,
"逐渐":0,
"通常":0,
"通过":0,
"造成":0,
"遇到":0,
"遭到":0,
"遵循":0,
"遵照":0,
"避免":0,
"那个":0,
"那么":0,
"那么些":0,
"那么样":0,
"那些":0,
"那会儿":0,
"那儿":0,
"那时":0,
"那末":0,
"那样":0,
"那般":0,
"那边":0,
"那里":0,
"那麽":0,
"部分":0,
"鄙人":0,
"采取":0,
"里面":0,
"重大":0,
"重新":0,
"重要":0,
"鉴于":0,
"针对":0,
"长期以来":0,
"长此下去":0,
"长线":0,
"长话短说":0,
"问题":0,
"间或":0,
"防止":0,
"附近":0,
"陈年":0,
"限制":0,
"陡然":0,
"除了":0,
"除却":0,
"除去":0,
"除外":0,
"除开":0,
"除此":0,
"除此之外":0,
"除此以外":0,
"除此而外":0,
"除非":0,
"随后":0,
"随时":0,
"随着":0,
"随著":0,
"隔夜":0,
"隔日":0,
"难得":0,
"难怪":0,
"难说":0,
"难道":0,
"难道说":0,
"集中":0,
"需要":0,
"非但":0,
"非常":0,
"非徒":0,
"非得":0,
"非特":0,
"非独":0,
"顶多":0,
"顷刻":0,
"顷刻之间":0,
"顷刻间":0,
"顺着":0,
"顿时":0,
"风雨无阻":0,
"首先":0,
"马上":0,
"高低":0,
"高兴":0,
"默然":0,
"默默地":0,
}
dic_prattle_why={
1:"您的问题暂时无法回答，能否请您换个话题？",
2:"您的问题范围有点大，能否缩小一下范围？",
3:"不太理解，什么是最重要的？",
4:"也许，还是不太明白。",
5:"问得有点深，机器人头脑烧傻，请跟换主题，谢谢！",
6:"好像漏了点什么，能否再详细些？",
7:"信息量有点少，请在补充一点吧？",
9:"信息量太大，请讲讲重点好么？",
10:"不可思议，有点不会了......",
}

# 最后无答案回复字典 打哈哈
dic_prattle_last={
1:"我听到了!",
2:"你是在和我说话么？",
3:"继续说，我在听。",
4:"哈哈，真是非常有趣的谈话。",
5:"后来呢？",
6:"确实如此。",
7:"应该可以。",
8:"嗯。",
9:"哦。",
10:"呵呵......",
11:"哈哈......",
12:"......",
13:"好的",
14:"OK",
15:"没能理解，能换个说法么？",
16:"请继续......",
17:"嗯,有可能。",
18:"我能理解。",
19:"哦，可以...",
20:"嗯，可以...",
}

# 问候语搭配字典
dic_hello ={
"你好":"你好，有什么可以帮到您？",
"早上好":"早上好，有什么可以帮到您？",
"晚上好":"晚上好，有什么可以帮到您？",
"上午好":"上午好，有什么可以帮到您？",
"中午好":"中午好，有什么可以帮到您？",
"下午好":"下午好，有什么可以帮到您？",
"再见":"再见",
"在":"在",
"忙么":"不忙啊",
"hello":"hello",
"bye":"bye",
"谢谢":"不客气",
"sorry":"Never mind",
}

# 问候型引导词
dic_guide ={
"您好":0,
"麻烦您":0,
"辛苦了":0,
"谢谢":0,
"请问?":0,
"请继续":0,
"请稍等":0,
"请指教":0,
"请原谅":0,
"见外了":0,
"美极了":0,
"真漂亮":0,
"甭客气":0,
"没关系":0,
"欢迎您":0,
"有劳您":0,
"晚上好":0,
"早上好":0,
"拜托了":0,
"您贵姓":0,
"您好":0,
"恭喜":0,
"忙么":0,
"很抱歉":0,
"很好":0,
"对不起":0,
"对不住":0,
"好的":0,
"失礼了":0,
"太棒了":0,
"太好了":0,
"多关照":0,
"多保重":0,
"在？":0,
"回头见":0,
"嗯。":0,
"嗯":0,
"哦。":0,
"有劳了":0,
"劳驾":0,
"别客气":0,
"再见":0,
"借光":0,
"你好":0,
"中午好":0,
"不错":0,
"不要紧":0,
"不用送":0,
"不用谢":0,
"不敢当":0,
"下午好":0,
"上午好":0,
"Sorry":0,
"OK":0,
"hello":0,
"bye":0,
"......":0,
}

# 命名实体识别高级字典
dic_ner_1 ={
"瘤":28608,
"癌":24171,
"肿":6205,
}

# 命名实体识别中级字典
dic_ner_2 ={
"淋巴":5935,
"放疗":815,
"化疗":2195,
"靶向药":1,
"手术":5055,
"病理":462,
"活多久":878,
"恶性":3036,
"良性":1418,
"早期":1146,
"晚期":2523,
"中期":242,
"白血病":148,
}

def main():
    print("") # 防止代码外泄 只输出一个空字符

if __name__ == '__main__':
    main()