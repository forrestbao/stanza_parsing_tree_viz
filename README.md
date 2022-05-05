# Stanza NLP parsing tree visualizer 
A simple Python function to beautifully print parsing trees from Stanza NLP toolbox

This is a simple Python function to beautifully print parsing trees from Stanza NLP toolbox. 
Many NLP toolboxes will output parsing results in S-expressions like below: 

```
(ROOT (S (NP (DT This)) (VP (VBZ is) (NP (DT a) (NN test)))))
```

It is not readable. SpaCy has a visualizer but Stanza does not. So I cranked this myself. 
This script will convert it into something much more readable like this: 

```
0_(ROOT 
1 |_(S 
2 | |_(NP 
3 | | |_(DT This)) 
2 | |_(VP 
3 | | |_(VBZ is) 
3 | | |_(NP 
4 | | | |_(DT a) 
4 | | | |_(NN test))) 
2 | |_(. .)))
```

# Use with Stanza for English

```python
import stanza 
stanza_nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency')
sentence = "After plugging into the outlet, you may press the I/O button"
doc = stanza_nlp(sentence)
for sent in doc.sentences:
    bracket_sent = str(sent.constituency)

print (bracket_sent)
print_parsing(bracket_sent)
```

```
(ROOT (S (PP (IN After) (S (VP (VBG plugging) (PP (IN into) (NP (DT the) (NN outlet)))))) (, ,) (NP (PRP you)) (VP (MD may) (VP (VB press) (NP (DT the) (NNP I/O) (NN button))))))

0_(ROOT 
1 |_(S 
2 | |_(PP 
3 | | |_(IN After) 
3 | | |_(S 
4 | | | |_(VP 
5 | | | | |_(VBG plugging) 
5 | | | | |_(PP 
6 | | | | | |_(IN into) 
6 | | | | | |_(NP 
7 | | | | | | |_(DT the) 
7 | | | | | | |_(NN outlet)))))) 
2 | |_(, ,) 
2 | |_(NP 
3 | | |_(PRP you)) 
2 | |_(VP 
3 | | |_(MD may) 
3 | | |_(VP 
4 | | | |_(VB press) 
4 | | | |_(NP 
5 | | | | |_(DT the) 
5 | | | | |_(NNP I/O) 
5 | | | | |_(NN button))))))

```


# Use with Stanza for Simplified Chinese

```python
stanza_nlp = stanza.Pipeline(lang='zh-hans', processors='tokenize,pos,constituency')
sentence = "通过主控计算机接通开关后, 应收到箭上配电器反馈的加电好信号。"
doc = stanza_nlp(sentence)
for sent in doc.sentences:
    bracket_sent = str(sent.constituency)

print (bracket_sent)
print_parsing(bracket_sent)
```

```
ROOT (IP (PP (IN 通过) (LCP (IP (NP (NN 主控) (VV 计算) (SFN 机)) (VP (VCD (VV 接通) (NN 开关)))) (NN 后,))) (VP (VRD (VV 应收) (VV 到)) (NP (CP (CP (IP (NP (LCP (NP (NN 箭)) (IN 上)) (VP (VP (VV 配) (NP (NN 电器))) (VP (VV 反馈))))) (DEC 的))) (NP (VV 加电)) (ADJP (PFA 好)) (NP (NN 信号)))) (. 。)))

0_(ROOT 
1 |_(IP 
2 | |_(PP 
3 | | |_(IN 通过) 
3 | | |_(LCP 
4 | | | |_(IP 
5 | | | | |_(NP 
6 | | | | | |_(NN 主控) 
6 | | | | | |_(VV 计算) 
6 | | | | | |_(SFN 机)) 
5 | | | | |_(VP 
6 | | | | | |_(VCD 
7 | | | | | | |_(VV 接通) 
7 | | | | | | |_(NN 开关)))) 
4 | | | |_(NN 后,))) 
2 | |_(VP 
3 | | |_(VRD 
4 | | | |_(VV 应收) 
4 | | | |_(VV 到)) 
3 | | |_(NP 
4 | | | |_(CP 
5 | | | | |_(CP 
6 | | | | | |_(IP 
7 | | | | | | |_(NP 
8 | | | | | | | |_(LCP 
9 | | | | | | | | |_(NP 
10 | | | | | | | | | |_(NN 箭)) 
9 | | | | | | | | |_(IN 上)) 
8 | | | | | | | |_(VP 
9 | | | | | | | | |_(VP 
10 | | | | | | | | | |_(VV 配) 
10 | | | | | | | | | |_(NP 
11 | | | | | | | | | | |_(NN 电器))) 
9 | | | | | | | | |_(VP 
10 | | | | | | | | | |_(VV 反馈))))) 
6 | | | | | |_(DEC 的))) 
4 | | | |_(NP 
5 | | | | |_(VV 加电)) 
4 | | | |_(ADJP 
5 | | | | |_(PFA 好)) 
4 | | | |_(NP 
5 | | | | |_(NN 信号)))) 
2 | |_(. 。)))
```
