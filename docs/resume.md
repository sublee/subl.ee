Title: Résumé: Heungsub Lee

Heungsub Lee
============

Contact {: .label }
: [heungsub.lee@subl.ee](mailto:heungsub.lee@subl.ee)
  or
  [+82 10-3215-2380](sms:821032152380)
  {: .attr }

Web Sites {: .label }
: [Homepage](/),
  [GitHub Profile](https://github.com/sublee),
  [LinkedIn Profile](https://linkedin.com/in/sublee)
  {: .attr }
{^ .attrs }

---

Interests
---------

- Parallel and distributed deep learning
- Developing and documentating API for engineers
- Free and open source software

Skills
------

Programming Languages {: .label }
: Python (expert), Go, JavaScript, Bash, C#
  {: .attr }

AI Research {: .label }
: PyTorch, NVIDIA Nsight Systems, Data/model/pipeline Parallelism
  {: .attr }

Back-end Developement {: .label }
: Linux, AWS, Terraform, Docker, ZeroMQ, Redis, etcd, MySQL
  {: .attr }

Test Engineering {: .label }
: Testify, mypy, pytest, GitLab CI, Travis CI
  {: .attr }
{^ .attrs }

---

Work Experience
---------------

Software Engineer {: .label }
[Kakao Brain][kakao-brain], 2018--
:   A deep learning artificial intelligence laboratory in Kakao.
    {: .note }

:   Focus on parallel and distributed deep learning to boost the training
    speed.

    Reproduced [GPipe][], which is a pipeline parallelism framework with
    checkpointing by Google, in PyTorch and implemented [torchgpipe][] as a
    library.

Game Server Architect {: .label }
What! Studio in [Nexon][], 2013--2018
:   Developing <cite>[Durango][]</cite>, a seamless open world MMORPG.
    {: .note }

:   Designed and implemented the architecture of a distributed MMORPG server.
    Achieved up to 70k concurrent users per MMO world. Launched the game and
    maintained it.

    Built an internationalization and localization system focused on
    linguistics features of Korean and Indo-European languages.

Game Development Engineer {: .label }
Team Lupin in [Nexon][], 2011--2013
:   Developed and launched two multiplayer racing games: <cite>[KartRider][]
    Dash & Coin Rush</cite>
    {: .note }

:   Designed and implemented a distributed game server architecture for
    synchronous multiplayer racing games. Launched the games globally and
    maintained them.

    Researched various rating systems such as [Elo][], [Glicko][], and
    [TrueSkill][]. Implemented a simple matchmaker for 4v4 or free-for-all
    racing games.

Full Stack Web Developer {: .label }
[Npine][], 2008--2011
:   Supplies stock images for business on <cite>[Iclickart][]</cite>.
    {: .note }

:   Developed a web server framework adapting the MVC pattern by PHP5.
    Maintained physical Linux machines in a data center. Led the software
    engineering team.

Front-end Web Developer {: .label }
[Lunant][], 2008--2011
:   Served <cite>VLAAH</cite>, a social network service for discovering,
    sharing, and utilizing opinions.
    {: .note }

:   Designed and implemented the UI/UX for <cite>VLAAH</cite> by PHP5,
    JavaScript with MooTools, and Python. Developed [jDoctest][], which tests
    JavaScript examples in doc comments, by JavaScript.

Open Source Experience
----------------------

[torchgpipe][], 2019--
:   [GPipe][] for PyTorch. GPipe is a scalable pipeline parallelism library for
    training of a giant model.
    {: .note }

:   Implemented the library with handy interface for easy integration by deep
    learning researchers or engineers. Reproduced the benchmarks in the GPipe
    paper.

[Hangulize][], 2010--
:   Automatically transcribes a non-Korean word into Hangul.
    {: .note }

:   Implemented the library to realize [Brian Jongseong Park's idea]
    [hangulize-idea]. Originally, wrote it in Python. But rewrote it in Go to
    achieve better features, performance, and productivity.

    Designed and implemented the web service and RESTful API. Professional
    Korean translators usually visit here to translate undocumented proper
    nouns. For example, Netflix refers this project in [the Korean timed text
    style guide][netflix-style].

[TrueSkill][trueskill-py], 2012--
:   A Python implementation of [TrueSkill™][trueskill] which is a rating
    algorithm for Xbox Live.
    {: .note }

:   Implemented TrueSkill™ by Python with simple API to learn and share the
    smart algorithm.

[Profiling][], 2014--2018
:   An interactive profiler for Python inspired by the Unity3D profiler.
    {: .note }

:   Developed to find bottlenecks in the <cite>[Durango][]</cite> server by
    Python and C. Designed a handy interactive TUI like [htop][] by [Urwid][].

    On GitHub, 2800+ people stared this project. Also it was the 3rd daily
    trending repository at Sep 22, 2014.

Others
:   - [Tossi][] -- A utility for Korean allomorphic particles.
    - [SUBLEERUNKER][] -- A simple prody game of SUBERUNKER.
                          Play it in your web browser.
    - [Flask-AutoIndex][] -- mod_autoindex for Flask
    - [Me2virus][] -- An XSS attack on [Me2day][], a social network service.
                      When a user looks an infected post, a new infected post
                      was written on the user's wall.

Contributed
:   [awesome-go#2104](https://github.com/avelino/awesome-go/pull/2104);
    [Babel#427](https://github.com/python-babel/babel/pull/427),
    [#488](https://github.com/python-babel/babel/pull/488);
    [base65536#2](https://github.com/Parkayun/base65536/pull/2);
    [couchbase-python-client#32](https://github.com/couchbase/couchbase-python-client/pull/32),
    [#33](https://github.com/couchbase/couchbase-python-client/pull/33),
    [#35](https://github.com/couchbase/couchbase-python-client/pull/35);
    [etcd#4320](https://github.com/coreos/etcd/pull/4320);
    [Flask-0.10.1](https://github.com/mitsuhiko/flask/commit/6fca662);
    [gevent#608](https://github.com/gevent/gevent/pull/608);
    [jQuery-1.4.3](https://blog.jquery.com/2010/10/16/jquery-143-released/);
    [node-irc#3](https://github.com/martynsmith/node-irc/pull/3);
    [pytest-rerunfailures#47](https://github.com/pytest-dev/pytest-rerunfailures/pull/47);
    [PyTorch#21006](https://github.com/pytorch/pytorch/pull/21006),
    [#21192](https://github.com/pytorch/pytorch/pull/21192);
    [PyZMQ#951](https://github.com/zeromq/pyzmq/pull/951);
    [TensorFlow#24678](https://github.com/tensorflow/tensorflow/pull/24678).

Invited Talks
-------------

- [Remake of Hangulize][gokr1808] at Golang Korea Meetup Aug 2018 (Korean)
- [The server architecture of Durango Vol. 3][ndc18] at NDC 2018 (Korean)
- [Python Survival Guide][nxtk16] at Nexon Talk 2016 (Korean)
- [The server architecture of Durango Vol. 2][ndc16] at NDC 2016,
  awarded the grand prize (Korean)
- [Profiling][pycon15] at PyCon KR 2015 (Korean)
- [The server architecture of Durango][ndc14] at NDC 2014 (Korean)

[ndc18]: https://subl.ee/~ndc18
[ndc16]: https://subl.ee/~ndc16
[ndc14]: https://subl.ee/~ndc14

[gokr1808]: https://subl.ee/~gokr1808
[nxtk16]:   https://subl.ee/~nxtk16
[pycon15]:  https://subl.ee/~pycon15

---

Languages
---------

- Korean -- native
- English -- pre-intermediate

Education
---------

Computer Software, [Kwangwoon University][kw], 2008
-- Completed the first year and left in mid course.

<!-- links -->
[gpipe]: https://arxiv.org/abs/1811.06965
[torchgpipe]: https://github.com/kakaobrain/torchgpipe
[durango]: http://durango.nexon.com/
[elo]: https://en.wikipedia.org/wiki/Elo_rating_system
[flask-autoindex]: http://pythonhosted.org/Flask-AutoIndex
[glicko]: https://en.wikipedia.org/wiki/Glicko_rating_system
[hangulize-idea]: http://iceager.egloos.com/2610028
[hangulize]: https://hangulize.org/
[htop]: http://hisham.hm/htop
[iclickart]: http://iclickart.co.kr/
[jdoctest]: https://lunant.github.com/jdoctest
[kakao-brain]: https://kakaobrain.com/
[kartrider]: http://kart.nexon.com/
[kw]: http://www.kw.ac.kr/
[lunant]: http://lunant.net/
[me2day]: https://en.wikipedia.org/wiki/Me2day
[me2virus]: https://github.com/sublee/me2virus
[netflix-style]: https://partnerhelp.netflixstudios.com/hc/en-us/articles/216001127-Korean-Timed-Text-Style-Guide
[nexon]: https://company.nexon.com/eng
[npine]: http://en.npine.com/
[profiling]: https://github.com/what-studio/profiling
[subleerunker]: /runker/
[tossi]: https://github.com/what-studio/tossi
[trueskill-py]: https://trueskill.org/
[trueskill]: http://research.microsoft.com/en-us/projects/trueskill/
[urwid]: http://urwid.org/
[vindictus]: https://en.wikipedia.org/wiki/Vindictus

<!-- abbrs -->
*[AWS]: Amazon Web Services
*[MMORPG]: Massively multiplayer online role-playing game
*[MVC]: Model-view-controller
*[NDC]: Nexon Developers Conference
*[TUI]: Text-based User Interface
*[XSS]: Cross-site Scripting
