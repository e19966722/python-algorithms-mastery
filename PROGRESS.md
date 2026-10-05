# 🚀 Python Software Engineering & Algorithmic Mentorship

## 🎯 Վերջնական նպատակ
**Python Backend + Applied AI / AI Automation Developer** (Remote / International Freelance / Official High-Paying Engineering Roles)։

---

## 📐 Ուսումնական Կանոնադրություն (Charter & Rules)
1. **Լեզուն**՝ Խիստ հայերեն բացատրություններ + տեխնիկական անգլերեն տերմիններ զուգահեռ (Technical English)։
2. **Առավելագույն Խորություն (Deep Internals, ոչ մի մակերեսայնություն)**՝ Բացատրել մինչև CPython-ի, PVM-ի, `PyObject`-ի և RAM հիշողության մակարդակ։ Ոչինչ չի խնայվում. բացատրվում են բոլոր edge-case-երը, տակից աշխատանքի մեխանիզմներն ու թակարդները։
3. **Անընդհատ Կրկնություն և Հետադարձ Հարցադրումներ (Spaced Repetition & Active Recall)**՝ Երբեք չենթադրել, որ մեկ անգամ յուրացված թեման ընդմիշտ հիշվելու է։ Յուրաքանչյուր դասին հետ ենք գնալու և տալու ենք հարցեր, Bug Hunt (գտնել սխալը) և բարդ իրավիճակներ անցած բոլոր թեմաներից։
4. **Լուծման տրամադրում**՝ Լուծումները միանգամից ՉԵՆ տրվում։ Օգնության հերթականություն՝
   `Small hint` ➡️ `Direction` ➡️ `Specific hint` ➡️ `Partial explanation` ➡️ `Full solution (միայն վերջում)`։
5. **Լուծումների վերլուծություն**՝ Correctness, Edge cases, Readability, Time/Space Complexity ($O$), Optimization, Pythonic practices + Interview questions։
6. **Թույլ կետերի վերահսկում**՝ Թույլ կետերը գրանցվում են Review Queue-ում և անընդհատ նորից են տրվում քողարկված տեսքով։

---

## ⏱️ Ժամերի և Առաջընթացի Գրանցամատյան (Session Tracker)

### Ընդհանուր վիճակագրություն
* **Ընդհանուր աշխատած ժամեր**՝ **6.8 ժամ (408 րոպե)**
* **Ընդհանուր լուծված խնդիրներ**՝ **18 լուրջ ալգորիթմական խնդիր** (բոլորը ✅)
* **Լիովին ինքնուրույն լուծված բարդ խնդիրներ**՝ 16 խնդիր
* **Մոտակա մեծ ստուգողական (40-50 ժամից)**՝ Մնացել է ~38 ժամ

---

## 🗺️ Python Core & Engineering Master Roadmap (Մինչև ՕՕՊ-ն ընկած ծրագիրը)

### ՄՈԴՈՒԼ 1․ Python-ի Ներքին Մեխանիզմը և Հիշողությունը (Internal Architecture & Memory)
- [ ] CPython, Bytecode (`.pyc`), PVM (Python Virtual Machine)
- [ ] `PyObject` կառուցվածքը C-ում, `id()` և `type()`
- [ ] Փոփոխականը որպես հղում (Reference vs Variable label)
- [ ] Mutability (Mutable vs Immutable), օբյեկտի փոփոխությունը հիշողության մեջ
- [ ] Integer caching (-5-ից 256) և String interning
- [ ] `is` (հասցեների նույնականություն) ընդդեմ `==` (արժեքների հավասարություն)
- [ ] Dynamic Array, Over-allocation list-ում, `sys.getsizeof()`

### ՄՈԴՈՒԼ 2․ Բազմաչափ Կառուցվածքներ և Թակարդներ (Nested Data & Hash Tables)
- [ ] Մատրիցներ (2D lists / list of lists), `matrix[row][col]`, Nested loops
- [ ] ⚠️ Թակարդ՝ `[[0] * 3] * 3` vs `[[0 for _ in range(3)] for _ in range(3)]`
- [ ] Slicing և Shallow vs Deep Copy (`copy.copy()` vs `copy.deepcopy()`)
- [ ] Բարդ Nested JSON/API տվյալների մշակում (List of Dicts, Nested Dicts)
- [ ] Hash Tables, `__hash__`, ինչու են միայն immutable-ները hashable, Hash Collisions

### ՄՈԴՈՒԼ 3․ Pythonic Իտերացիա և Կառավարում (Comprehensions & Advanced Flow)
- [ ] List, Dict, Set comprehensions (ներդրված comprehensions, մատրիցի տրանսպոնացում)
- [ ] `enumerate()`, `zip()`, `any()`, `all()`
- [ ] `sorted(key=lambda)` (տեսակավորում ըստ կոնկրետ դաշտի / սյան)
- [ ] Short-circuit evaluation (`and` / `or`), `for...else`, `match...case`

### ՄՈԴՈՒԼ 4․ Ֆունկցիաների Առաջադեմ Կիրառում և Ֆունկցիոնալ Ծրագրավորում
- [ ] First-class citizens (ֆունկցիան որպես արգումենտ և վերադարձվող արժեք)
- [ ] `*args`, `**kwargs`, positional-only (`/`), keyword-only (`*`)
- [ ] ⚠️ Թակարդ՝ Default mutable arguments (`def add(item, lst=[])`)
- [ ] LEGB Scoping (Local, Enclosing, Global, Built-in), `global` և `nonlocal`
- [ ] Lambda, `map()`, `filter()`
- [ ] Closures (Փականներ) և Դեկորատորներ (`@decorator`, `@wraps`)

### ՄՈԴՈՒԼ 5․ Իտերատորներ, Գեներատորներ և Հիշողության Խնայողություն
- [ ] Iterable vs Iterator, `iter()`, `next()`
- [ ] `yield`, Generator functions, Lazy evaluation
- [ ] Generator expressions `(x for x in data)`

### ՄՈԴՈՒԼ 6․ Բացառություններ, Ֆայլեր և Մոդուլայնություն
- [ ] `try...except...else...finally`, Built-in Exception Hierarchy
- [ ] Context Managers (`with open(...) as f:`), ռեսուրսների արտահոսք
- [ ] Մոդուլներ, փաթեթներ, import կառուցվածք, `if __name__ == '__main__':`

---

## 🧠 Թույլ կետեր և Կրկնության ենթակա թեմաներ (Review Queue — Active Recall)
1. **Boolean Logic (`and` vs `or`)** — Ուշադրություն `while a != 1 and a != 4` տիպի պայմաններին։
2. **Անվերջ ցիկլերի դետեկցիա (Cycle Detection)** — Երբ թիվը չի վերադառնում սկզբնական արժեքին, այլ պտտվում է միջանկյալ շրջանում։
3. **Nested Loops Complexity** — Ցիկլի ներսում `.count()` կամ `.remove()` կանչելիս գիտակցել $O(n^2)$ բարդությունը և փոխարինել $O(n)$ բառարաններով կամ Two Pointers-ով։
4. **Ցուցակների Հղումներ vs Պատճեններ (Reference vs Shallow Copy)** — Հիշել, որ Python-ում `b = a` ցուցակը չի պատճենում, այլ ստեղծում է երկրորդ հղում նույն հիշողությանը: Պատճենելու համար անհրաժեշտ է `a.copy()` կամ `a[:]`:
5. **Ցուցակի ձևափոխում ցիկլի ընթացքում (Mutating list during iteration)** — Ցուցակից տարր ջնջելը հենց այդ ցուցակի վրայով պտտվող `for` ցիկլում բերում է ինդեքսների տեղաշարժի (index shift) և հարևան տարրերի բացթողման:

