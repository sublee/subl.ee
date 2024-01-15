title: Résumé: Heungsub Lee
description: A résumé of Heungsub Lee, a software engineer

Heungsub Lee
============

Contact {: .label }
: [heungsub@subl.ee](mailto:heungsub@subl.ee)
  {: .attr }

Web Sites {: .label }
: [subl.ee](/),
  [github.com/sublee](https://github.com/sublee),
  [linkedin.com/in/sublee](https://linkedin.com/in/sublee)
  {: .attr }

---

Skills
------

Programming Languages {: .label }
: Go, Python, TypeScript, Bash
  {: .attr }

Service Development {: .label }
: Linux, AWS, K8s, React, ZeroMQ, NoSQL, Concurrent programming, Testing, CI/CD
  {: .attr }

ML Engineering {: .label }
: PyTorch, NVIDIA Nsight Systems, NCCL
  {: .attr }

---

Work Experience
---------------

Software Engineer {: .label }
[Global AI Platform][gapco], Sep 2023 -- Present
:   Focusing on making everyone utilize AI for their daily productivity.
    Developed and maintained the client and server of [Gistty][], a Chrome
    extension summarizing Amazon reviews.

[gapco]: https://www.globalaiplatform.com/
[gistty]: https://gistty.ai/

Software Engineering Manager {: .label }
[NAVER][], Aug 2020 -- Jul 2023
:   Supervised MLOps platforms by leading 25 software engineers to optimize the
    inference performance and productivity of [HyperCLOVA][], an LLM
    specializing in Korean culture.

    Developed the second version of [NSML][], an ML research platform in
    [CLOVA][], to extend its capability for large-scale AI models on HPC
    infrastructures.

[naver]: https://navercorp.com/en
[hyperclova]: https://clova.ai/hyperclova
[nsml]: https://arxiv.org/abs/1712.05902
[clova]: https://clova.ai/

Software Engineer {: .label }
[Kakao Brain][kakaobrain], Dec 2018 -- Aug 2020
:   Developed and published a pipeline parallelism library named
    [torchgpipe][] in open source.

    Developed a serverless training framework and a distributed hyperparameter
    search platform for an AutoML service.

[kakaobrain]: https://kakaobrain.com/
[torchgpipe]: https://torchgpipe.readthedocs.io/
[gpipe]: https://arxiv.org/abs/1811.06965

Game Server Engineer {: .label }
[NEXON][], Mar 2011 -- Dec 2018
:   Developed cloud-based distributed MMORPG servers for Durango using pub/sub
    communication over the spatial grid system. Achieved up to 70k concurrent
    users per game world.

    Developed online racing game servers and matchmaking for [KartRider][] Dash
    and KartRider Coin Rush.

[nexon]: https://company.nexon.com/en/
[kartrider]: https://kart.nexon.com/

Back-end Web Developer {: .label }
[nPine][iclickart], Dec 2008 -- Feb 2011
:   Developed web services selling stock images.
[iclickart]: https://iclickart.co.kr/

Front-end Web Developer {: .label }
[Lunant][], Dec 2007 -- Jan 2011
:   Designed and developed UI/UX for social media.
[lunant]: https://github.com/lunant

Open Source Experience
----------------------

[torchgpipe][], Feb 2019 -- Apr 2020
:   Implemented [GPipe][], a multi-GPU pipeline parallelism technique for
    training giant models, as a PyTorch library with optimization for CUDA, the
    autograd engine, and long skip connections. This project has become a part
    of PyTorch as [Pipe APIs][pytorch-pipe]

[torchgpipe]: https://torchgpipe.readthedocs.io/
[gpipe]: https://arxiv.org/abs/1811.06965
[pytorch-pipe]: https://pytorch.org/docs/2.0/pipeline.html

[Hangulize][], Oct 2010 -- Present
:   Invented a Hangul transcription algorithm and served as a web tool at zero
    cost. Many professional Korean translators use this tool to translate
    undocumented proper nouns.

[hangulize]: https://hangulize.org/

[TrueSkill][trueskill], Jan 2012 -- Dec 2015
:   Implemented [TrueSkill™][trueskill-tm], the rating algorithm for Xbox Live,
    as a Python library. This project was introduced in [PyData Berlin
    2019][pydata2019].

[trueskill]: https://trueskill.org/
[trueskill-tm]: https://www.microsoft.com/en-us/research/project/trueskill-ranking-system/
[pydata2019]: https://docs.google.com/presentation/d/1S5v9D31vpsr22efMSSCO6hmN2SQNCIqKG7JyGzUSzeI/edit?usp=sharing

Contributions
:   - For [PyTorch][],
      fixed potential GPU memory violation ([#27371][pytorch#27371]);
      deprecated inconsistent API ([#21006][pytorch#21006],
      [#25985][pytorch#25985]); discussed a counterintuitive behavior
      of the autograd engine ([#18568][pytorch#18568]).
    - For [ZeroMQ][],
      discussed a PUB socket crash ([#2942][zeromq#2942]).
    - For [Flask][],
      fixed a bug to generate a URL with a subdomain ([#108][flask#108]).
    - For [jQuery 1.4.3][jquery-143],
      fixed a bug on content negotiation in Ajax requests.

[pytorch]:       https://pytorch.org/
[pytorch#27371]: https://github.com/pytorch/pytorch/pull/27371
[pytorch#21006]: https://github.com/pytorch/pytorch/pull/21006
[pytorch#25985]: https://github.com/pytorch/pytorch/pull/25985
[pytorch#18568]: https://github.com/pytorch/pytorch/pull/18568
[zeromq]:        https://zeromq.org/
[zeromq#2942]:   https://github.com/zeromq/libzmq/issues/2942
[flask]:         https://flask.palletsprojects.com/
[flask#108]:     https://github.com/pallets/flask/issues/108
[jquery-143]:    https://blog.jquery.com/2010/10/16/jquery-143-released/

---

Publications
------------

<!-- IEEE style: https://libguides.nps.edu/citation/ieee -->
- B. Kim et al., "What changes can large-scale language models bring? Intensive
  study on HyperCLOVA: Billions-scale Korean generative pretrained
  Transformers," [arXiv:2109.04650][arxiv:hyperclova], Sep 2021.
- C. Kim\*, Heungsub Lee\* et al., "torchgpipe: On-the-fly pipeline parallelism
  for training giant models," [arXiv:2004.09910][arxiv:torchgpipe], Apr 2020.

\*Contributed equally
{: .footnote }

*[B. Kim]: Boseop Kim
*[C. Kim]: Chiheon Kim

[arxiv:hyperclova]: https://arxiv.org/abs/2109.04650
[arxiv:torchgpipe]: https://arxiv.org/abs/2004.09910

Public Speeches
---------------

<!-- Also, IEEE style -->
- "NSML, the hyper-scale ML training platform," [KRnet, Jun 2022][krnet22].
- "[Remake of Hangulize][gokr1808]," Golang Korea Meetup, Aug 2018.
- "[Profiling][pycon15]," PyCon Korea, Aug 2015.
- "The server architecture of Durango," NDC, [2014][ndc14], [2016][ndc16], and
  [2018][ndc18].

[krnet22]: https://www.kca.kr/boardView.do?boardId=NOTICE&seq=4600077

[gokr1808]: https://subl.ee/~gokr1808
[pycon15]:  https://subl.ee/~pycon15

[ndc18]: https://subl.ee/~ndc18
[ndc16]: https://subl.ee/~ndc16
[ndc14]: https://subl.ee/~ndc14

---

Languages
---------

- Korean --- Native
- English --- Conversant in reading and writing

Education
---------

Computer Software, [Kwangwoon University][kw], 2008, Completed the first year
only.

[kw]: https://www.kw.ac.kr/

<!-- abbrs -->
*[AWS]:    Amazon Web Services
*[K8s]:    Kubernetes
*[NCCL]:   NVIDIA Collective Communications Library
*[CI/CD]:  Continuous integration and continuous delivery
*[AI]:     Artificial intelligence
*[ML]:     Machine learning
*[HPC]:    High-performance computing
*[MMORPG]: Massively multiplayer online role-playing game
*[NDC]:    NEXON Developers Conference
*[Ajax]:   Asynchronous JavaScript and XML
