---
schema_version: will-ai-question-bank/v1
source_pdf: SWA_R00_FA2026-C1N.pdf
source_sha256: 91f032cd253112733c358f45d78c24847a5b7dbe35105f1028b39252d65f87ac
source_pages: 32
question_bank_version: V1
product_scope: SWA
---

# SWA_R00_FA2026-C1N 题库与判定标准

## 1. Source Information

- Source PDF: `SWA_R00_FA2026-C1N.pdf`
- SHA-256: `91f032cd253112733c358f45d78c24847a5b7dbe35105f1028b39252d65f87ac`
- Physical pages: 32
- Product: KOSMEK SWA 气动涨紧下拉夹紧器
- Product printed pages: 693-718
- Included common-reference printed pages: 925-928, 947-948
- Source-evidence policy: PDF page images control visual facts; OCR is a navigation aid and is not source truth.

## 2. Scope

### 2.1 Product and document scope

This bank covers the SWA pneumatic double-acting expanding pull-down clamp series:
purpose and mechanism, SWA1000/SWA2000 bodies, straight-hole and tapered-hole
forms, workpiece-lift and no-pull-down variants, model grammar, specifications,
force formulae and curves, dimensions, installation, pneumatic circuits, sensing,
design and operating cautions, maintenance, and applicable common-reference
material included in the PDF.

Warranty terms and sales-network material are retained in the inventory but excluded
from core capability questions because they are commercial metadata rather than
durable SWA technical knowledge.

### 2.2 Model Grammar

The PDF defines separate straight-hole and tapered-hole forms.

Straight-hole pattern:

`SWA<BodySize>00<DesignNo>-<Lift>-<HoleCode>-<SeatHeight?>-<ClawShape?>-<Option?>`

Tapered-hole pattern:

`SWA<BodySize>00<DesignNo>-<Lift>-<HoleCode>-<SeatHeight?>-T`

An optional blank field is represented by the unmarked position between separators.
Fields must stay in the printed order and follow these rules.

| Field | Legal values | Meaning and constraint |
|---|---|---|
| BodySize | `1`, `2` | Selects SWA1000 or SWA2000. |
| Fixed digits | `00` | Fixed digits printed between body size and design number. |
| DesignNo | `0` | Product version/design number listed by this PDF. |
| Lift | `A`, `N` | `A` lifts the released workpiece 0.2 mm; `N` has no workpiece-lift function. Use `N` when combined with the listed expanding locating pins. |
| Straight HoleCode for BodySize `1` | `060`, `065`, `070`, `075`, `080`, `085`, `090` | Straight workpiece holes phi 6-9 mm in 0.5 mm steps. |
| Straight HoleCode for BodySize `2` | `090`, `095`, `100`, `105`, `110`, `115`, `120`, `125`, `130` | Straight workpiece holes phi 9-13 mm in 0.5 mm steps. |
| Tapered HoleCode for BodySize `1` | `065`, `070`, `075`, `080`, `085`, `090` | Tapered holes phi 6.5-9 mm; code `060` is forbidden. |
| Tapered HoleCode for BodySize `2` | `090`, `095`, `100`, `105`, `110`, `115`, `120`, `125`, `130` | Tapered holes phi 9-13 mm. |
| SeatHeight | blank, `H35`, `H40`, `H45`, `H50`, `H55`, `H60` | Blank is the standard 30 mm height; explicit nonstandard heights use 5 mm steps. `H30` is not the printed notation. |
| Straight ClawShape | blank, `F` | Blank is serrated for strong internal-wall clamping; `F` is non-serrated. |
| Tapered ClawShape | `T` | Tapered-hole form is serrated and uses the terminal `T`; `F` is unavailable. |
| Straight Option | blank, `W` | Blank is the standard pull-down form; `W` has no pull-down function, no seating-confirmation air port, and no lift spring. `W` requires Lift `N`. |

Additional model constraints:

- The tapered-hole form has no `W` option field and permits a taper angle up to 3 degrees; below 1 degree requires consultation with KOSMEK.
- Straight SWA1000 codes `060` and `065` are limited to 0.5 MPa maximum supply pressure.
- Tapered SWA1000 codes `065` and `070` are limited to 0.5 MPa maximum supply pressure.
- No-pull-down SWA1000 code `060` or `065`, with or without `F`, is limited to 0.5 MPa maximum supply pressure.
- Straight-hole object tolerance depends on Lift: `A` uses phi d +/-0.3 mm; `N` uses phi d +0.7/-0.3 mm.
- Tapered-hole tolerance depends on body, hole code, and taper-angle band; it must be taken from the printed table rather than inferred from the straight-hole rule.

Positive grammar cases:

- `SWA1000-N-065-H45-F-W`
- `SWA1000-A-090--T`
- `SWA2000-N-130-H60-F-W`

Negative grammar cases and reasons:

- `SWA1000-A-060--T`: tapered form forbids hole code `060`.
- `SWA1000-A-065-H45-F-W`: option `W` requires Lift `N`.
- `SWA1000-N-095-H40-F-W`: code `095` is outside the SWA1000 range.
- `SWA2000-N-085-H40-F-W`: code `085` is outside the SWA2000 range.
- `SWA1000-N-070-H45-F-T`: tapered `T` cannot be combined with straight non-serrated `F`.
- `SWA1000-N-070-H30-F-W`: standard 30 mm height uses a blank field, not `H30`.
- `SWA1001-N-065-H45-F-W`: design number `1` is not listed.
- `SWA1000-N-065-H45-F-X`: option `X` is not listed.

### 2.3 Source-first inventory and WP4 coverage dispositions

`HIGH` and `MEDIUM` items are mapped to tested questions or given an explicit scoped
disposition. The WP4 construction audit checks that every mapping resolves to an
existing question and that no high-value testable object remains unresolved.

| Inventory ID | Physical / printed page | Local scope | Evidence type | Priority | Testable object | Initial disposition |
|---|---|---|---|---|---|---|
| SWA-SI-001 | 1 / 693 | Product introduction > operating principle | TEXT + DRAWING | HIGH | Expand against the workpiece-hole wall, then pull the workpiece down for clamping | `SWA-Q-0002` |
| SWA-SI-002 | 2 / 694 | Features > fixture and machining benefits | TEXT + DRAWING | MEDIUM | Shorter tool overhang, improved machining accuracy, compact fixture/rotary-table examples | No separate question: application-benefit examples are derivative outcomes, not stable operating or selection rules |
| SWA-SI-003 | 3 / 695 | Features > body and application range | TEXT + TABLE + DRAWING | HIGH | SWA/SWE/SWH installation-size boundary; two body sizes; variable seat height and hole diameter | `SWA-Q-0003`; product-comparison illustration is contextual only |
| SWA-SI-004 | 4 / 696 | Features > seating and no-pull-down applications | TEXT + DRAWING | HIGH | Seating reference, positioning behavior, and W-form deformation-control use | `SWA-Q-0005`, `SWA-Q-0025` |
| SWA-SI-005 | 5 / 697 | Features > protection and cleaning | TEXT + DRAWING | HIGH | Protective cap, small sliding clearance, air-cleaning effect, replaceable claw, and rough-guide conditions | `SWA-Q-0004`; detailed handling controls in `SWA-Q-0023` |
| SWA-SI-006 | 6 / 698 | Features > self-lock and pull-down mechanism | TEXT + DRAWING | HIGH | Spring clamp/self-lock at zero pressure, pull-down travel, and simplified internal structure | `SWA-Q-0005`, `SWA-Q-0019` |
| SWA-SI-007 | 7 / 699 | Features > workpiece lift and confirmation | TEXT + DRAWING | HIGH | Lift-option dependency, lift travel, action confirmation, excessive lift, and broken-rod states | Lift dependency in `SWA-Q-0001`/`0006`; state diagnosis in `SWA-Q-0020` |
| SWA-SI-008 | 8 / 700 | Operating principle and sensing states | STATE_DIAGRAM + TEXT | HIGH | Release/clamp sequences, pull-down threshold, seating confirmation, continuous air supply, and abnormal-state detection | `SWA-Q-0019`, `SWA-Q-0020` |
| SWA-SI-009 | 9-10 / 701-702 | Model designation > straight-hole form | TABLE + DRAWING | HIGH | Seven-field order, body/lift/hole/height/claw/option meanings, body-hole ranges, and W dependencies | `SWA-Q-0001`, `SWA-Q-0003` |
| SWA-SI-010 | 11-12 / 703-704 | Model designation > tapered-hole form | TABLE + DRAWING | HIGH | Six-field order, terminal T, legal holes, angle-dependent tolerances, serration rule, and unavailable options | `SWA-Q-0006`, `SWA-Q-0007` |
| SWA-SI-011 | 13 / 705 | Specifications > straight-hole form | TABLE | HIGH | A/N hole tolerances, eccentric allowance, travel, lift force, air volume, pressure, temperature, fluid, and special pressure limits | `SWA-Q-0001`, `SWA-Q-0008`, `SWA-Q-0009` |
| SWA-SI-012 | 14 / 706 | Specifications > tapered-hole form | TABLE | HIGH | Taper angle/tolerance binding, eccentric allowance, travel, capacity, pressure, and unavailable 060 code | `SWA-Q-0006` through `SWA-Q-0009` |
| SWA-SI-013 | 15 / 707 | Standard form > clamping-force table, formula, and chart | FORMULA + CHART + TABLE | HIGH | Force-pressure relationships for serrated/T and F forms, spring force at 0 MPa, and restricted pressure ranges | `SWA-Q-0015`, `SWA-Q-0017` |
| SWA-SI-014 | 16 / 708 | W form > expansion-force table, formula, and chart | FORMULA + CHART + TABLE | HIGH | Expansion-force relationships, friction assumption, 0 MPa spring force, 0.1 mm maximum pull-down, and pressure limits | `SWA-Q-0016`, `SWA-Q-0018` |
| SWA-SI-015 | 17-18 / 709-710 | SWA1000 outline and mounting dimensions | DRAWING + TABLE | HIGH | Released/full-stroke geometry, workpiece/mounting-hole machining, height variants, ports, mass, and interference cautions | `SWA-Q-0010`; thin-wall/interference risks consolidated in `SWA-Q-0022` |
| SWA-SI-016 | 19-20 / 711-712 | SWA2000 outline and mounting dimensions | DRAWING + TABLE | HIGH | Released/full-stroke geometry, workpiece/mounting-hole machining, height variants, ports, mass, and interference cautions | `SWA-Q-0010`; thin-wall/interference risks consolidated in `SWA-Q-0022` |
| SWA-SI-017 | 21 / 713 | Configuration example > SWA-N with VWM | DRAWING + TEXT | HIGH | D/C locating-pin arrangement, rough-guide design, SWA vertical orientation, and mandatory Lift N selection | `SWA-Q-0011`, `SWA-Q-0021` |
| SWA-SI-018 | 22 / 714 | Pneumatic-circuit examples | STATE_DIAGRAM + TABLE + TEXT | HIGH | One/two-solenoid circuits, VWM-before-SWA sequence, speed-control fallback, sensor-per-clamp rule, sensing states, and failure consequences | `SWA-Q-0021` |
| SWA-SI-019 | 23 / 715 | Design cautions > unpowered state and seating | TEXT + DRAWING | HIGH | Spring-clamped zero-pressure state, release-air requirement for loading, Z datum, full-seat contact, and seating confirmation | Unpowered state in `SWA-Q-0005`; release/clamp procedure in `SWA-Q-0019`; seating risks in `SWA-Q-0022` |
| SWA-SI-020 | 23 / 715 | Design cautions > force and workpiece constraints | TEXT + DRAWING | HIGH | Trial clamping, insufficient-force drop risk, hole size/depth/taper/hardness limits, thin-wall deformation, and continuous cleaning/sensing air | `SWA-Q-0022` covers hole-design constraints; `SWA-Q-0028` covers thin-wall trial clamping; `SWA-Q-0024` covers continuous cleaning/sensing air |
| SWA-SI-021 | 24 / 716 | Handling cautions > horizontal and manual loading | TEXT + DRAWING | HIGH | Pre-clamping for horizontal use, no tilted/floating loading, fully released loading, small support clearance, and rough guides | `SWA-Q-0023`; horizontal pre-clamp is a documented application-specific addition |
| SWA-SI-022 | 24 / 716 | Robot handling | TEXT + DRAWING | HIGH | Perpendicular insertion/removal, complete withdrawal before coordinate motion, controlled insertion speed, and motion interlock | `SWA-Q-0023` |
| SWA-SI-023 | 25 / 717 | Installation > air, cleaning, tape, bolts, and ports | TEXT + TABLE | HIGH | Filtered dry air/no lubrication, pre-cleaning, tape practice, M5 class 12.9 at 6.3 N-m, port identities, and phi 6/4 minimum tubing | `SWA-Q-0024` |
| SWA-SI-024 | 25 / 717 | Operation safety | TEXT | HIGH | Qualified operator, anti-drop/anti-motion controls, zero-energy disassembly, cooling, restart inspection, pinch avoidance, no modification, and spring hazard | `SWA-Q-0027`; spring-disassembly hazard in `SWA-Q-0026`; product-local rules control over common appendix |
| SWA-SI-025 | 26 / 718 | SWA maintenance and claw replacement | TEXT + TABLE | HIGH | Cleaning clamp/seat surfaces, contamination consequences, manufacturer overhaul, wear replacement, and 1,000,000/500,000-cycle reference values | `SWA-Q-0012`, `SWA-Q-0026` |
| SWA-SI-026 | 27 / 925 | Common pneumatic appendix > operation and maintenance | TEXT | MEDIUM | Shared zero-energy safety, cleaning, leak/sound/motion checks, storage, and overhaul rules | No separate question: shared safety rules are duplicated and more locally bound in `SWA-Q-0026` and `SWA-Q-0027`; appendix retained as corroboration only |
| SWA-SI-027 | 28 / 926 | Common appendix > warranty | TEXT | LOW | Warranty term, coverage, and exclusions | Exclude from core capability bank; low-value commercial policy |
| SWA-SI-028 | 29 / 927 | Common appendix > surface roughness notation | TABLE | MEDIUM | 2021 old/new JIS notation mapping | `SWA-Q-0013` (`DOCUMENT_COMMON`) |
| SWA-SI-029 | 30 / 928 | Common appendix > O-ring notation | TABLE + MODEL | MEDIUM | New/old notation mapping and field meanings | `SWA-Q-0014` (`DOCUMENT_COMMON`) |
| SWA-SI-030 | 31-32 / 947-948 | Sales addresses and network | TEXT + DRAWING | NON-TEST | Contact details, sales geography, and certification marks | Exclude; not durable SWA technical knowledge |

## 3. Question Statistics

- Total: 28
- FACT: 4
- SPEC_LOOKUP: 2
- TABLE: 5
- MODEL: 3
- CALCULATION: 2
- CHART: 2
- PROCEDURE: 4
- CAUTION: 6

## 4. Questions

## SWA-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA1000-N-065-H45-F-W

### Question

请按 PDF 的直孔型号字段顺序，解读 `SWA1000-N-065-H45-F-W` 的主体尺寸、
设计编号、工件提升方式、工件孔径及孔公差、着座高度、涨爪形状和选配功能；
同时给出该组合的最高使用压力，并判断字段组合是否合法。

### Standard Answer

`SWA1000` 的主体尺寸字段为 `1`，适用直径 phi 6-9 mm 的工件孔；固定数字
后面的设计编号为 `0`。`N` 表示无工件提升功能。孔径符号 `065` 表示直孔
phi 6.5 mm；Lift `N` 对应的对象孔公差为 +0.7/-0.3 mm。`H45` 表示着座高度
45 mm。`F` 表示直孔用无锯齿涨爪。`W` 表示无下拉功能，并且该选配必须与
Lift `N` 组合。SWA1000 的 `060`/`065` 无下拉型号最高使用压力为 0.5 MPa。
因此该型号的字段顺序、各字段取值和依赖关系均合法。

### Scoring Standard

- P1 [5]: 正确识别主体尺寸 `1` 对应 SWA1000。
- P2 [5]: 正确给出 SWA1000 的直孔范围 phi 6-9 mm。
- P3 [5]: 正确识别设计编号为 `0`。
- P4 [10]: 正确解释 `N` 为无工件提升功能。
- P5 [10]: 正确解释 `065` 为直孔 phi 6.5 mm。
- P6 [10]: 正确给出 Lift `N` 下的孔公差 +0.7/-0.3 mm。
- P7 [10]: 正确解释 `H45` 为 45 mm 着座高度。
- P8 [10]: 正确解释 `F` 为直孔用无锯齿涨爪。
- P9 [10]: 正确解释 `W` 为无下拉功能。
- P10 [10]: 明确 `W` 必须与 Lift `N` 组合。
- P11 [10]: 正确给出最高使用压力 0.5 MPa。
- P12 [5]: 明确得出完整字段组合合法的结论。

### Accepted Variants

- `phi 6.5 mm` 可写为 `φ6.5 mm`、`Φ6.5 mm` 或 `直径 6.5 mm`。
- 公差可等价写为上偏差 `+0.7 mm`、下偏差 `-0.3 mm`。
- `无下拉功能` 可写为 `不执行下拉`，但不得与无提升功能混淆。

### Forbidden Errors

- 将 `N` 解释为无下拉功能，或将 `W` 解释为无工件提升功能。
- 将 `F` 解释为锥孔代码或有锯齿涨爪。
- 将对象孔公差写为 +/-0.3 mm；该公差属于 Lift `A`，不是本型号的 `N`。
- 将本型号最高使用压力写为 0.7 MPa。
- 在 `W` 与非 `N` 提升字段组合时仍判定合法。

### Tolerance

- Exact model fields, hole tolerance, and 0.5 MPa pressure limit are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 9-10, 13, 16
- Printed page: 701-702, 705, 708
- Section: 型号表示（工件孔形状：直孔） / 规格（工件孔形状：直孔） / 能力曲线图（W：无下拉功能）
- Local scope path: 直孔型号字段图 > SWA1000 / N / 065 / H45 / F / W；直孔规格表 > N 孔公差；W 能力页 > SWA1000 060/065 压力限制
- Evidence type: TABLE + DRAWING
- Evidence: 型号页按主体尺寸、设计编号、提升方式、孔径、着座高度、涨爪形状和选配项排列字段；表格定义 N、065、H45、F 和 W，并规定 W 必须选择 N；规格与 W 能力页将 SWA1000 的 060/065 型号最高压力限制为 0.5 MPa。

## SWA-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 系列基本夹紧原理

### Question

请说明 SWA 气动涨紧下拉夹紧器从释放状态到夹紧完成的三个基本阶段，
并明确涨爪作用的工件部位和完成夹紧的运动方向。

### Standard Answer

释放状态用于搬入或搬出工件。开始夹紧后，涨爪先向外涨紧工件对象孔的
内壁。随后夹紧器沿下拉方向拉动工件，使工件下拉并完成夹紧。

### Scoring Standard

- P1 [30]: 正确说明释放状态用于工件搬入或搬出。
- P2 [35]: 正确说明夹紧过程中涨爪向外涨紧对象孔内壁。
- P3 [35]: 正确说明最终沿下拉方向拉动工件完成夹紧。

### Accepted Variants

- `对象孔内壁` 可写为 `工件孔内壁`。
- `下拉工件` 可写为 `将工件拉向着座面`。

### Forbidden Errors

- 将涨爪作用位置写成工件外周或孔外壁。
- 省略涨紧孔内壁而直接描述为仅靠轴向压紧。
- 将完成夹紧的方向写成向上提升。

### Tolerance

- N/A

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 1
- Printed page: 693
- Section: 产品说明 / 动作原理（涨紧下拉夹紧器顶端部位）
- Local scope path: 页首产品说明 > 动作原理三状态图 > 释放状态 / 夹紧过程中 / 夹紧完成
- Evidence type: TEXT + DRAWING
- Evidence: 三状态图将工件搬入/搬出、涨紧对象孔内壁以及下拉工件完成夹紧按顺序表示。

## SWA-Q-0003

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA1000/SWA2000 直孔规格选择范围与着座高度系列

### Question

请给出 SWA1000 和 SWA2000 可选的直孔孔径范围、孔径增量，以及两种主体
尺寸共同的标准着座高度和可指定着座高度系列。标准 30 mm 高度应如何写入型号？

### Standard Answer

SWA1000 的直孔孔径范围为 phi 6-9 mm，SWA2000 为 phi 9-13 mm，孔径均按
0.5 mm 增量选择。两种主体尺寸的标准着座高度都是 30 mm；指定高度为
35、40、45、50、55、60 mm，对应 `H35` 至 `H60`，按 5 mm 增量。
标准 30 mm 高度在型号中使用空白字段，不写 `H30`。

### Scoring Standard

- P1 [20]: 正确给出 SWA1000 的直孔范围 phi 6-9 mm。
- P2 [20]: 正确给出 SWA2000 的直孔范围 phi 9-13 mm。
- P3 [15]: 正确给出孔径增量 0.5 mm。
- P4 [15]: 正确给出标准着座高度 30 mm。
- P5 [10]: 正确列出指定高度 35-60 mm。
- P6 [10]: 正确说明指定高度每 5 mm 一档。
- P7 [10]: 明确标准 30 mm 使用空白字段而不是 `H30`。

### Accepted Variants

- `phi` 可写为 `φ`、`Φ` 或 `直径`。
- 指定高度可等价写为 `H35/H40/H45/H50/H55/H60`。

### Forbidden Errors

- 将 SWA1000 的上限写成 13 mm，或将 SWA2000 的下限写成 6 mm。
- 将孔径或高度增量写成 1 mm。
- 将标准高度型号字段写为 `H30`。

### Tolerance

- Exact ranges and increments are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 3, 9-12
- Printed page: 695, 701-704
- Section: 特点 / 型号表示（直孔、锥孔）
- Local scope path: 特点 > 工件孔直径尺寸和着座面高度；型号表示 > 主体尺寸 / 工件孔径 / 着座高度尺寸
- Evidence type: TABLE + TEXT + DRAWING
- Evidence: 特点页与型号表共同给出两种主体尺寸的孔径范围、0.5 mm 孔径增量、30 mm 标准高度和 H35-H60 指定高度。

## SWA-Q-0004

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 系列保护套、滑动间隙与工件搬运特性

### Question

SWA 系列如何通过防护帽和微小滑动间隙应对切削粉尘与冷却液？该结构对
工件搬入/搬出及粗导销设置有什么影响？

### Standard Answer

SWA 全型号附带防护帽。微小滑动间隙可防止切削粉尘等异物侵入，并提高
喷气清洁效果；即使空气流量较小，也能有效防止冷却液侵入。搬运时工件
与涨爪不接触，因此工件可以顺畅搬入/搬出。夹具通常无需设置粗导销，
但是否省略仍取决于搬入速度等实际条件。

### Scoring Standard

- P1 [15]: 明确全型号附带防护帽。
- P2 [20]: 正确说明微小滑动间隙用于防止切削粉尘等异物侵入。
- P3 [15]: 正确说明微小间隙提高喷气清洁效果。
- P4 [20]: 正确说明少量空气流量也可有效防止冷却液侵入。
- P5 [8]: 正确说明搬运时工件与涨爪不接触。
- P6 [7]: 正确说明无接触结构使工件可顺畅搬入/搬出。
- P7 [8]: 正确说明粗导销通常可省略。
- P8 [7]: 正确保留是否省略仍需结合搬入速度等实际条件判断的限定。

### Accepted Variants

- `防护帽` 可写为 `保护帽`。
- `微小滑动间隙` 可写为 `小滑动间隙`。

### Forbidden Errors

- 声称防护帽只用于某一个主体尺寸。
- 声称不需要喷气或该结构能在任意污染条件下完全密封。
- 无条件断言任何应用都禁止或无需使用粗导销。

### Tolerance

- N/A

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 5
- Printed page: 697
- Section: 特点 > 可实现全面防护的保护套结构
- Local scope path: 防护帽结构 > 滑动间隙 / 清洁效果 / 工件搬入搬出 / 粗导销条件
- Evidence type: TEXT + DRAWING
- Evidence: 页面明确标示全型号防护帽、微小间隙的防尘和喷气清洁作用，以及无接触搬运和粗导销的条件性省略。

## SWA-Q-0005

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 标准下拉型与 W 无下拉型的弹簧和夹紧差异

### Question

请比较 SWA 标准下拉型与 `W` 无下拉型的弹簧配置、夹紧运动和零气压状态。

### Standard Answer

标准下拉型内置提升弹簧和夹紧弹簧：提升弹簧帮助涨紧工件孔内壁，随后
机构把工件下拉到着座面；即使气压降为零，夹紧弹簧仍提供自锁保持。
`W` 无下拉型不设置提升弹簧，只以扩径力夹紧，并将轴向下拉限制在最多
0.1 mm；它仍有夹紧弹簧和零气压自锁功能。

### Scoring Standard

- P1 [15]: 正确指出标准型内置提升弹簧。
- P2 [20]: 正确指出标准型涨紧后把工件下拉到着座面。
- P3 [20]: 正确指出夹紧弹簧在零气压时提供自锁保持。
- P4 [10]: 正确指出 W 型无提升弹簧。
- P5 [10]: 正确指出 W 型只以扩径力夹紧。
- P6 [10]: 正确指出 W 型轴向下拉最多 0.1 mm。
- P7 [7]: 正确指出 W 型仍有夹紧弹簧。
- P8 [8]: 正确指出 W 型在零气压时仍可自锁保持。

### Accepted Variants

- `零气压自锁` 可写为 `供给压力为零时仍保持夹紧`。
- `最多 0.1 mm` 可写为 `0.1 mm 以下`。

### Forbidden Errors

- 声称标准型仅扩径而不下拉。
- 声称 W 型具有正常 1.0 mm 下拉行程或提升弹簧。
- 声称零气压时夹紧弹簧立即释放工件。

### Tolerance

- Exact 0.1 mm upper limit is required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 4, 6, 13
- Printed page: 696, 698, 705
- Section: 特点 > 无下拉功能型 / 自锁与下拉；规格（直孔）
- Local scope path: 标准与 W 对比图 > 提升弹簧 / 夹紧弹簧；规格表 > 工件下拉行程
- Evidence type: TEXT + DRAWING + TABLE
- Evidence: 特点页区分标准型与 W 型的弹簧和运动，规格表将标准下拉行程列为 1.0 mm、W 列为 0.1 mm 以下。

## SWA-Q-0006

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA2000-A-125-H55-T

### Question

请按锥孔型号字段顺序解读 `SWA2000-A-125-H55-T`，包括主体尺寸、设计编号、
工件提升方式、对象孔径、着座高度和涨爪形状；给出最高使用压力，并判断
该字段组合是否合法。

### Standard Answer

`SWA2000` 的主体尺寸字段为 `2`，适用锥孔孔径 phi 9-13 mm；设计编号为
`0`。`A` 表示有工件提升功能，释放时提升 0.2 mm。`125` 表示对象锥孔
phi 12.5 mm。`H55` 表示着座高度 55 mm。终端 `T` 表示锥孔用有锯齿涨爪；
锥孔型号没有 `F` 或 `W` 字段。该 SWA2000 组合最高使用压力为 0.7 MPa，
各字段顺序和值合法。实际孔公差还必须结合锥孔勾配角查表，不能仅凭型号确定。

### Scoring Standard

- P1 [10]: 正确识别主体尺寸 `2` 为 SWA2000。
- P2 [10]: 正确给出 SWA2000 锥孔范围 phi 9-13 mm。
- P3 [5]: 正确识别设计编号 `0`。
- P4 [10]: 正确解释 `A` 为有工件提升功能。
- P5 [10]: 正确给出提升行程 0.2 mm。
- P6 [10]: 正确解释 `125` 为 phi 12.5 mm 锥孔。
- P7 [10]: 正确解释 `H55` 为 55 mm 着座高度。
- P8 [5]: 正确解释 `T` 为锥孔用有锯齿涨爪。
- P9 [3]: 正确说明锥孔型号没有 `F` 字段。
- P10 [2]: 正确说明锥孔型号没有 `W` 字段。
- P11 [10]: 正确给出最高使用压力 0.7 MPa。
- P12 [5]: 正确判定完整字段组合合法。
- P13 [5]: 正确说明孔公差仍依赖勾配角查表。
- P14 [5]: 字段解读保持锥孔型号的印刷顺序。

### Accepted Variants

- `勾配角` 可写为 `锥度角` 或 `taper angle`。
- `有锯齿` 可写为 `serrated`。

### Forbidden Errors

- 将 `T` 解释为直孔无锯齿 `F`。
- 为锥孔型号添加 `W` 选配项。
- 将 `125` 解释为 12.5 mm 直孔而忽略终端 `T`。
- 将最高使用压力写成 0.5 MPa。
- 在未给出勾配角时声称已唯一确定孔公差。

### Tolerance

- Exact model fields, 0.2 mm lift, and 0.7 MPa pressure are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 11-12, 14
- Printed page: 703-704, 706
- Section: 型号表示（工件孔形状：锥孔） / 规格（工件孔形状：锥孔）
- Local scope path: 锥孔型号字段图 > SWA2000 / A / 125 / H55 / T；锥孔规格表 > 最高使用压力
- Evidence type: TABLE + DRAWING
- Evidence: 锥孔型号页定义六字段顺序、孔径范围、提升、着座高度和 T 涨爪；规格表给出 SWA2000 的 0.7 MPa 最高压力。

## SWA-Q-0007

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA1000/SWA2000 锥孔型号的勾配角与工件孔径公差表

### Question

按 PDF 的锥孔公差表分别给出以下允许公差：SWA1000-080 在 2.5 度和
2.8 度、SWA1000-090 在 2.3 度和 2.8 度、SWA2000-125 在 2.5 度和
2.8 度。勾配角不足 1 度时应如何处理？

### Standard Answer

- SWA1000-080，2.5 度：phi d +/-0.3 mm。
- SWA1000-080，2.8 度：phi d +0.3/-0.15 mm。
- SWA1000-090，2.3 度：phi d +0.3/-0.15 mm。
- SWA1000-090，2.8 度：phi d +0.3/0 mm。
- SWA2000-125，2.5 度：phi d +/-0.3 mm。
- SWA2000-125，2.8 度：phi d +0.3/-0.15 mm。
- 勾配角不足 1 度时，应垂询 KOSMEK，不能从该表自行外推。

### Scoring Standard

- P1 [15]: 正确给出 SWA1000-080、2.5 度的 +/-0.3 mm。
- P2 [15]: 正确给出 SWA1000-080、2.8 度的 +0.3/-0.15 mm。
- P3 [15]: 正确给出 SWA1000-090、2.3 度的 +0.3/-0.15 mm。
- P4 [15]: 正确给出 SWA1000-090、2.8 度的 +0.3/0 mm。
- P5 [15]: 正确给出 SWA2000-125、2.5 度的 +/-0.3 mm。
- P6 [15]: 正确给出 SWA2000-125、2.8 度的 +0.3/-0.15 mm。
- P7 [5]: 正确说明勾配角不足 1 度时需垂询 KOSMEK。
- P8 [5]: 正确说明不得从表内区间自行外推不足 1 度的公差。

### Accepted Variants

- `phi d` 可写为 `φd`。
- `+/-0.3 mm` 可写为上偏差 `+0.3 mm`、下偏差 `-0.3 mm`。
- 下偏差为零可写为 `+0.3/0 mm` 或 `0 至 +0.3 mm`。

### Forbidden Errors

- 对所有锥孔统一套用 +/-0.3 mm。
- 混淆 SWA1000-090 的 2.5 度分界与 065-085 的分界。
- 将 2.8 度时 SWA1000-090 的下偏差写成 -0.15 mm。
- 对不足 1 度直接给出表内公差。

### Tolerance

- Exact upper and lower deviations are required; angle inputs are exact table lookups.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 11
- Printed page: 703
- Section: 型号表示（工件孔形状：锥孔）
- Local scope path: 工件孔勾配角与工件孔径的容许公差表 > SWA1000 065-085 / 090；SWA2000 095-130
- Evidence type: TABLE
- Evidence: 表格按主体尺寸、孔径代码和勾配角区间分别绑定上/下偏差，并在表下注明不足 1 度需垂询。

## SWA-Q-0008

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA1000/SWA2000 直孔规格的偏心量、行程和提升能力

### Question

请比较 SWA1000 与 SWA2000 直孔型号的对象工件硬度、容许偏心量、全行程、
标准型和 W 型工件下拉行程，以及 A 型工件提升行程和提升力。

### Standard Answer

两种主体尺寸的对象工件硬度均为 HB250 以下，全行程均为 4.2 mm。
SWA1000 的容许偏心量为 +/-0.3 mm，SWA2000 为 +/-0.5 mm。标准型工件
下拉行程为 1.0 mm，W 型为 0.1 mm 以下。A 型工件提升行程均为 0.2 mm；
提升力为 SWA1000 0.09 kN、SWA2000 0.15 kN。

### Scoring Standard

- P1 [10]: 正确给出两种主体尺寸的对象工件硬度为 HB250 以下。
- P2 [10]: 正确给出 SWA1000 容许偏心量 +/-0.3 mm。
- P3 [10]: 正确给出 SWA2000 容许偏心量 +/-0.5 mm。
- P4 [15]: 正确给出共同全行程 4.2 mm。
- P5 [15]: 正确给出标准型下拉行程 1.0 mm。
- P6 [15]: 正确给出 W 型下拉行程 0.1 mm 以下。
- P7 [10]: 正确给出 A 型提升行程 0.2 mm。
- P8 [7]: 正确给出 SWA1000 提升力 0.09 kN。
- P9 [8]: 正确给出 SWA2000 提升力 0.15 kN。

### Accepted Variants

- `HB250 以下` 可写为 `不高于 HB250`。
- `0.1 mm 以下` 可写为 `最大 0.1 mm`。

### Forbidden Errors

- 交换两种主体尺寸的容许偏心量或提升力。
- 将 W 型下拉行程写成标准型的 1.0 mm。
- 声称 N 型也具有 0.2 mm 工件提升行程。

### Tolerance

- Exact values and units are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 13
- Printed page: 705
- Section: 规格（工件孔形状：直孔）
- Local scope path: 直孔规格表 > 对象工件硬度 / 容许偏心量 / 行程 / 提升力
- Evidence type: TABLE
- Evidence: 规格表按 SWA1000/SWA2000 列给出硬度、偏心量、全行程、标准/W 下拉行程以及仅 A 型适用的提升行程和提升力。

## SWA-Q-0009

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA1000/SWA2000 直孔和锥孔规格中的气容量与共通气源环境

### Question

请给出 SWA1000、SWA2000 空动作时释放侧和夹紧侧的夹紧器容量，并给出
系列共同的最低释放压力、推荐喷气清洁压力、工作温度范围和使用流体。

### Standard Answer

SWA1000 的释放侧容量为 4.8 cm3，夹紧侧为 4.3 cm3；SWA2000 的释放侧
为 7 cm3，夹紧侧为 6.1 cm3。共同最低释放压力为 0.25 MPa，推荐喷气
清洁压力为 0.2-0.3 MPa，工作温度范围为 0-70 degrees C，使用流体为干燥空气。

### Scoring Standard

- P1 [10]: 正确给出 SWA1000 释放侧容量 4.8 cm3。
- P2 [10]: 正确给出 SWA1000 夹紧侧容量 4.3 cm3。
- P3 [10]: 正确给出 SWA2000 释放侧容量 7 cm3。
- P4 [10]: 正确给出 SWA2000 夹紧侧容量 6.1 cm3。
- P5 [15]: 正确给出最低释放压力 0.25 MPa。
- P6 [15]: 正确给出推荐喷气清洁压力 0.2-0.3 MPa。
- P7 [15]: 正确给出工作温度范围 0-70 degrees C。
- P8 [15]: 正确给出使用流体为干燥空气。

### Accepted Variants

- `cm3` 可写为 `cm^3` 或 `立方厘米`。
- `0.2-0.3 MPa` 可写为 `0.2 至 0.3 MPa`。
- `干燥空气` 可写为 `dry air`。

### Forbidden Errors

- 交换释放侧与夹紧侧容量。
- 交换 SWA1000 与 SWA2000 的容量。
- 将最低释放压力写成最高使用压力。
- 将使用流体写成油雾润滑空气或液压油。

### Tolerance

- Exact values and units are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 13-14
- Printed page: 705-706
- Section: 规格（工件孔形状：直孔、锥孔）
- Local scope path: 规格表 > 夹紧器容量（空动作时）/ 最低释放压力 / 推荐喷气清洁用气压 / 工作温度 / 使用流体
- Evidence type: TABLE
- Evidence: 直孔和锥孔规格表对两种主体尺寸给出相同的气容量与共通气源环境值。

## SWA-Q-0010

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA1000/SWA2000 外形尺寸表中的着座高度 H、尺寸 AA 和重量

### Question

根据外形尺寸表，比较 SWA1000 与 SWA2000 在标准着座高度和 `H60` 时的
H 尺寸与重量，并给出 `H60` 对应的 AA 尺寸。

### Standard Answer

标准着座高度时 H 为 30 mm，`H60` 时 H 为 60 mm；`H60` 对应 AA 为
30.5 mm。SWA1000 标准高度重量为 0.7 kg，H60 为 0.75 kg；SWA2000
标准高度重量为 1.0 kg，H60 为 1.1 kg。

### Scoring Standard

- P1 [10]: 正确给出标准 H 尺寸 30 mm。
- P2 [10]: 正确给出 H60 的 H 尺寸 60 mm。
- P3 [15]: 正确给出 H60 的 AA 尺寸 30.5 mm。
- P4 [15]: 正确给出 SWA1000 标准高度重量 0.7 kg。
- P5 [15]: 正确给出 SWA1000 H60 重量 0.75 kg。
- P6 [15]: 正确给出 SWA2000 标准高度重量 1.0 kg。
- P7 [15]: 正确给出 SWA2000 H60 重量 1.1 kg。
- P8 [3]: H 与 AA 尺寸使用 mm。
- P9 [2]: 重量使用 kg。

### Accepted Variants

- `1.0 kg` 可写为 `1 kg`。
- `标准着座高度` 可写为 `无符号高度`。

### Forbidden Errors

- 将 AA 30.5 mm 当作 H 尺寸。
- 交换 SWA1000 与 SWA2000 的重量。
- 将 H60 的高度解释为在标准 30 mm 上再增加 60 mm。

### Tolerance

- Exact table values and units are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 18, 20
- Printed page: 710, 712
- Section: 外形尺寸表以及安装部加工尺寸表
- Local scope path: SWA1000/SWA2000 外形尺寸页 > 着座高度尺寸表 > H / AA / 重量
- Evidence type: TABLE + DRAWING
- Evidence: 两个主体尺寸的着座高度表列出无符号、H35-H60 对应 H、AA 和各自重量。

## SWA-Q-0011

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA-N 与 VWM 扩径定位销组合配置参考

### Question

在 PDF 的 SWA-N 与 VWM 组合配置参考中，VWM-D、VWM-C 和 SWA 分别承担
什么角色？SWA 的提升方式和安装方向如何选择？粗导销的数量、直径间隙和
高出基板的参考尺寸是什么，何时可考虑省略？

### Standard Answer

VWM-D 是基准定位销，VWM-C 是菱形定位销；SWA-N 用于涨紧下拉夹紧。
与 VWM 组合时，SWA 必须选择 `N` 无工件提升功能，并垂直安装。为防止
装卸时损伤夹紧部位，参考配置设置 2 根以上粗导销；图示直径间隙为
1 mm 以下，粗导销高出基板 10 mm 以上。只有在根据工件搬入/搬出条件
确认可行时，才可考虑不设置粗导销。

### Scoring Standard

- P1 [15]: 正确说明 VWM-D 为基准定位销。
- P2 [15]: 正确说明 VWM-C 为菱形定位销。
- P3 [20]: 正确说明与 VWM 组合时 SWA 选择 N 无提升功能。
- P4 [10]: 正确说明 SWA 垂直安装。
- P5 [15]: 正确给出粗导销数量为 2 根以上。
- P6 [10]: 正确给出直径间隙 1 mm 以下。
- P7 [10]: 正确给出高出基板 10 mm 以上。
- P8 [5]: 正确保留按搬入/搬出条件才可省略粗导销的限定。

### Accepted Variants

- `基准定位销` 可写为 `圆销/基准销`，但必须与 VWM-D 绑定。
- `菱形定位销` 可写为 `diamond pin`，但必须与 VWM-C 绑定。

### Forbidden Errors

- 交换 VWM-D 与 VWM-C 的定位角色。
- 与 VWM 组合时选择 A 有提升功能。
- 将 SWA 水平安装，或无条件省略粗导销。
- 将 1 mm 以下写成 1 mm 以上。

### Tolerance

- Exact minimum/maximum qualifiers are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 21
- Printed page: 713
- Section: 配置（安装）参考范例
- Local scope path: SWA-N 与 VWM 组合图 > VWM-D / VWM-C / SWA-N / 粗导销；注意事项 1-2
- Evidence type: DRAWING + TEXT
- Evidence: 配置图标注定位销角色、SWA 垂直方向及粗导销几何值，页下注释规定 VWM 组合必须选择 N。

## SWA-Q-0012

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 涨爪磨损与更换参考次数表

### Question

PDF 对 A2017 铝材和 SCM435 H 材质分别给出什么涨爪更换参考次数？这些次数
是否是无条件固定寿命，发现涨爪表面磨损时应如何处理？

### Standard Answer

A2017 铝材的参考值为夹紧动作 100 万次，SCM435 H 材质为 50 万次。
这些不是无条件固定寿命；实际更换周期会随使用压力、工件材质、孔形状等
条件变化，应在实际机器上确认。发现涨爪表面磨损时必须更换涨爪，因为
磨损会降低夹紧力。

### Scoring Standard

- P1 [30]: 正确给出 A2017 铝材 100 万次参考值。
- P2 [30]: 正确给出 SCM435 H 材质 50 万次参考值。
- P3 [10]: 明确参考次数受压力、材质、孔形状等使用条件影响。
- P4 [10]: 明确参考次数不是无条件固定寿命。
- P5 [10]: 明确发现涨爪磨损时必须更换。
- P6 [10]: 正确说明更换原因是磨损会降低夹紧力。

### Accepted Variants

- `100 万次` 可写为 `1,000,000 cycles`。
- `50 万次` 可写为 `500,000 cycles`。

### Forbidden Errors

- 交换两种材质的参考次数。
- 将参考次数解释为保证寿命或强制在该次数前不得更换。
- 声称涨爪磨损不会影响夹紧力。

### Tolerance

- Exact cycle references and their conditional nature are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 26
- Printed page: 718
- Section: 保养・检查
- Local scope path: 保养・检查 > 项目 3 > 夹紧孔材质 / 涨爪更换基准表
- Evidence type: TEXT + TABLE
- Evidence: 表格列出两种材质的参考动作次数，正文说明周期受使用条件影响且磨损会降低夹紧力。

## SWA-Q-0013

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: SWA_R00_FA2026-C1N.pdf 共通附录
- Model / Scope: SWA_R00_FA2026-C1N.pdf :: printed page 927 表面粗糙度新旧标示对照表

### Question

按 PDF 的 2021 年表面粗糙度标示更改表，分别给出新标示 Rz 6.3、Rz 25、
Rz 100 的 Ra 参考值，以及各自对应的旧 JIS Rmax 范围。

### Standard Answer

- Rz 6.3：Ra 参考值 1.6；旧标示 1.6S-6.3S。
- Rz 25：Ra 参考值 6.3；旧标示 12.5S-25S。
- Rz 100：Ra 参考值 25；旧标示 50S-100S。
新标示依据 JIS B 0601:2013，旧标示依据 JIS B 0601:1982。

### Scoring Standard

- P1 [15]: 正确给出 Rz 6.3 的 Ra 参考值 1.6。
- P2 [15]: 正确给出 Rz 6.3 的旧范围 1.6S-6.3S。
- P3 [15]: 正确给出 Rz 25 的 Ra 参考值 6.3。
- P4 [15]: 正确给出 Rz 25 的旧范围 12.5S-25S。
- P5 [15]: 正确给出 Rz 100 的 Ra 参考值 25。
- P6 [15]: 正确给出 Rz 100 的旧范围 50S-100S。
- P7 [5]: 正确给出新标示依据 JIS B 0601:2013。
- P8 [5]: 正确给出旧标示依据 JIS B 0601:1982。

### Accepted Variants

- 范围连接符可写为 `~`、`至` 或短横线。
- `Ra 参考值` 不要求重复书写单位，但数值必须绑定正确 Rz 行。

### Forbidden Errors

- 把 Ra 参考值当作 Rmax 旧范围。
- 交换 Rz 25 与 Rz 100 的映射。
- 将该表错误绑定为 SWA 某一具体型号的专用规格。

### Tolerance

- Exact row mappings are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 29
- Printed page: 927
- Section: 表面粗糙度（表面性状）符号的标示更改
- Local scope path: 共通附录 > 2021 年标示更改 > 新 JIS B 0601:2013 / 旧 JIS B 0601:1982 对照表
- Evidence type: TABLE
- Evidence: 对照表逐行绑定 Rz、Ra 参考值及旧 Rmax 范围。

## SWA-Q-0014

**Type: MODEL**

### Target

- Binding: DOCUMENT_COMMON
- Product: SWA_R00_FA2026-C1N.pdf 共通附录
- Model / Scope: SWA_R00_FA2026-C1N.pdf :: printed page 928 O 形密封圈新旧标示与字段含义

### Question

请把新标示 `OR NBR-90 P5-N` 转换为 PDF 表中的旧 JIS 标示，并解释
`NBR-90`、`P`、`5` 和 `N` 四个字段的含义。

### Standard Answer

`OR NBR-90 P5-N` 对应旧 JIS 标示 `1BP5`。`NBR-90` 对应旧材料识别符号
`1B`，表示一般用丁腈橡胶、A 型硬度 90；`P` 是滑动用的种类标记；`5`
是公称号；末尾 `N` 是一般用品质等级。

### Scoring Standard

- P1 [15]: 正确转换为旧标示 `1BP5`。
- P2 [20]: 正确说明 `NBR-90` 对应旧材料符号 `1B`。
- P3 [10]: 正确说明材料为一般用丁腈橡胶。
- P4 [5]: 正确说明材料的 A 型硬度为 90。
- P5 [15]: 正确说明 `P` 表示滑动用。
- P6 [15]: 正确说明 `5` 为公称号。
- P7 [15]: 正确说明末尾 `N` 为一般用品质等级。
- P8 [5]: 保持材料、种类、公称号和品质等级的字段顺序与绑定。

### Accepted Variants

- `丁腈橡胶` 可写为 `NBR` 或 `nitrile rubber`。
- `A 型硬度 90` 可写为 `Shore A 90`。
- `公称号 5` 可结合种类写为 `P5`，但仍需说明 P 和 5 的不同字段含义。

### Forbidden Errors

- 转换为 `1AP5`；该旧标示对应 NBR-70-1，不是 NBR-90。
- 将 `P` 解释为压力等级。
- 将末尾 `N` 解释为材料代码或公称号。
- 将此共通附录规则声称为 SWA 专用型号语法。

### Tolerance

- Exact old designation and field meanings are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 30
- Printed page: 928
- Section: O 形密封圈的标示更改
- Local scope path: 共通附录 > O 形密封圈新旧标示比较 > OR NBR-90 P5-N / 1BP5；字段说明 1-4
- Evidence type: TABLE + MODEL
- Evidence: 对照表将新标示与旧 JIS 标示逐行映射，字段图解释材料识别、种类、公称号和品质等级。

## SWA-Q-0015

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA2000 标准有锯齿直孔型及 T 锥孔型夹紧力公式

### Question

SWA2000 标准有锯齿直孔型或 T 锥孔型的夹紧力公式为
`Fc = 1.43P + 0.1`，其中 `Fc` 的单位为 kN，供给气压 `P` 的单位为 MPa。
当 `P = 0.46 MPa` 时，计算夹紧力；中间值保留完整精度，最终使用
`ROUND_HALF_UP` 四舍五入到小数点后两位，并用表中相邻压力值做回代检查。

### Standard Answer

代入得 `Fc = 1.43 * 0.46 + 0.1 = 0.7578 kN`。使用 `ROUND_HALF_UP`
保留两位小数，最终为 `0.76 kN`。表中 0.4 MPa 对应 0.65 kN、0.5 MPa
对应 0.80 kN；0.76 kN 位于两者之间，与压力单调增加关系一致。

### Scoring Standard

- P1 [15]: 使用正确公式 `Fc = 1.43P + 0.1`。
- P2 [15]: 正确代入 `P = 0.46 MPa`。
- P3 [20]: 正确得到未舍入值 `0.7578 kN`。
- P4 [20]: 按 `ROUND_HALF_UP` 正确得到最终值 `0.76 kN`。
- P5 [5]: 输入气压明确使用 MPa。
- P6 [5]: 最终夹紧力明确使用 kN。
- P7 [6]: 正确使用 0.4 MPa 对应 0.65 kN 的表值。
- P8 [6]: 正确使用 0.5 MPa 对应 0.80 kN 的表值。
- P9 [8]: 正确确认计算结果位于 0.65-0.80 kN 之间。

### Accepted Variants

- 计算过程可使用等价的高精度十进制实现。
- 回代检查可表述为 `0.65 < 0.76 < 0.80 kN`。

### Forbidden Errors

- 使用 SWA1000 的 `0.93P + 0.1` 公式。
- 在乘法前提前舍入输入或系数。
- 将结果写成 N、MPa 或无单位数值。
- 将两位小数规则错误解释为 +/-0.01 的容差。

### Tolerance

- Final result must be exactly 0.76 kN after `ROUND_HALF_UP` to two decimal places; raw value must be 0.7578 kN.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 15
- Printed page: 707
- Section: 能力曲线图（选配项无符号：标准）
- Local scope path: 夹紧力表 > SWA2000 / SWA2000-T 列 > 夹紧力计算公式和 0.4/0.5 MPa 行
- Evidence type: FORMULA + TABLE
- Evidence: 页面将 SWA2000 有锯齿/T 系列绑定到 `Fc=1.43P+0.1`，并给出相邻压力的离散夹紧力值。

## SWA-Q-0016

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA1000-N-065 W 无下拉型扩径力与压力限制

### Question

孔径代码为 `065` 的 SWA1000 W 无下拉型使用扩径力公式
`FH = 2.71P + 0.5`。当供给气压为 `0.48 MPa` 时，计算扩径力；中间值
保留完整精度，最终使用 `ROUND_HALF_UP` 四舍五入到小数点后两位。
同时判断该压力对 `065` 型号是否合法，并用相邻表值检查结果。

### Standard Answer

`FH = 2.71 * 0.48 + 0.5 = 1.8008 kN`，两位小数结果为 `1.80 kN`。
SWA1000 W 型的 `060/065` 代码最高只能使用 0.5 MPa，因此 0.48 MPa 合法。
表中 0.4 MPa 为 1.6 kN、0.5 MPa 为 1.9 kN，1.80 kN 位于两者之间。

### Scoring Standard

- P1 [15]: 使用正确公式 `FH = 2.71P + 0.5`。
- P2 [15]: 正确代入 `P = 0.48 MPa`。
- P3 [20]: 正确得到未舍入值 `1.8008 kN`。
- P4 [20]: 按 `ROUND_HALF_UP` 正确得到最终值 `1.80 kN`。
- P5 [5]: 输入气压明确使用 MPa。
- P6 [5]: 最终扩径力明确使用 kN。
- P7 [10]: 正确判断 0.48 MPa 未超过 `065` 型号的 0.5 MPa 上限。
- P8 [4]: 正确使用 0.4 MPa 对应 1.6 kN 的表值。
- P9 [4]: 正确使用 0.5 MPa 对应 1.9 kN 的表值。
- P10 [2]: 正确确认计算结果位于两个相邻表值之间。

### Accepted Variants

- `1.80 kN` 可在说明两位小数规则后显示为数值 `1.80`，但不得省略单位。
- 合法性可写为 `0.48 <= 0.5 MPa`。

### Forbidden Errors

- 使用夹紧力公式而不是 W 型扩径力公式。
- 将 0.5 MPa 上限忽略或写成 0.7 MPa。
- 将最终值写成 1.8 MPa。
- 以公式替代相邻表值回代检查。

### Tolerance

- Final result must be exactly 1.80 kN after `ROUND_HALF_UP` to two decimal places; raw value must be 1.8008 kN.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 16
- Printed page: 708
- Section: 能力曲线图（选配项 W：无下拉功能）
- Local scope path: 扩径力表 > SWA1000-W 列 > 计算公式 / 0.4/0.5 MPa 行；注 5 > 060/065 压力限制
- Evidence type: FORMULA + TABLE
- Evidence: 页面将 SWA1000 W 系列绑定到 `FH=2.71P+0.5`，给出相邻表值，并限制 060/065 代码不得超过 0.5 MPa。

## SWA-Q-0017

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: 标准型夹紧力曲线中的 SWA2000/SWA2000-T 与 SWA1000-F 系列

### Question

只按 PDF 第 707 页夹紧力曲线做视觉读数：当供给气压为 `0.45 MPa` 时，
分别读取 `SWA2000/SWA2000-T` 实线和 `SWA1000-F` 虚线的夹紧力，并比较
两者大小。不得用离散表值直接冒充图表读数。

### Standard Answer

从横轴 0.45 MPa 向上读取，`SWA2000/SWA2000-T` 曲线约为 `0.74 kN`，
`SWA1000-F` 曲线约为 `0.14 kN`。前者明显大于后者，约高 `0.60 kN`。
这些 Gold 值来自曲线视觉读取；公式计算仅用于确认读数数量级合理。

### Scoring Standard

- P1 [8]: 正确识别横轴为供给气压 MPa。
- P2 [7]: 正确识别纵轴为夹紧力 kN。
- P3 [15]: 正确选中 SWA2000/SWA2000-T 实线系列。
- P4 [25]: 对该系列给出容差内的约 0.74 kN 读数。
- P5 [15]: 正确选中 SWA1000-F 虚线系列。
- P6 [20]: 对该系列给出容差内的约 0.14 kN 读数。
- P7 [5]: 正确判断 SWA2000/SWA2000-T 的读数更大。
- P8 [5]: 正确给出两条曲线读数差约 0.60 kN。

### Accepted Variants

- 允许读数在下述 CHART 容差内。
- 差值可写为约 0.6 kN，不要求多余小数位。

### Forbidden Errors

- 交换两条曲线或把虚线当作 SWA2000/SWA2000-T。
- 报告离散表中 0.4 或 0.5 MPa 的值而未读取 0.45 MPa。
- 将扩径力曲线页的 W 型数值用于本题。

### Tolerance

- CHART: SWA2000/SWA2000-T 0.74 kN +/-0.05 kN; SWA1000-F 0.14 kN +/-0.05 kN; input pressure is exactly 0.45 MPa.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 15
- Printed page: 707
- Section: 能力曲线图（选配项无符号：标准）
- Local scope path: 夹紧力曲线图 > 横轴 0.45 MPa > SWA2000/SWA2000-T 实线与 SWA1000-F 虚线
- Evidence type: CHART
- Evidence: 曲线图明确标示供给气压和夹紧力坐标轴及四条系列线；0.45 MPa 位于 0.4 与 0.5 网格线中间。

## SWA-Q-0018

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: W 无下拉型扩径力曲线中的 SWA2000-W 与 SWA1000-W 系列

### Question

只按 PDF 第 708 页 W 型扩径力曲线做视觉读数：供给气压为 `0.45 MPa` 时，
分别读取 `SWA2000-W` 和 `SWA1000-W` 的扩径力，并说明哪条曲线更高。

### Standard Answer

在 0.45 MPa 处，`SWA2000-W` 的扩径力约为 `2.50 kN`，`SWA1000-W`
约为 `1.72 kN`；SWA2000-W 曲线更高，差值约 `0.78 kN`。Gold 来自图表
视觉读取，公式只用于 sanity check。

### Scoring Standard

- P1 [8]: 正确识别横轴为供给气压 MPa。
- P2 [7]: 正确识别纵轴为扩径力 kN。
- P3 [15]: 正确识别上方曲线为 SWA2000-W。
- P4 [25]: 给出容差内的约 2.50 kN 读数。
- P5 [15]: 正确识别下方曲线为 SWA1000-W。
- P6 [20]: 给出容差内的约 1.72 kN 读数。
- P7 [5]: 正确判断 SWA2000-W 的读数更高。
- P8 [5]: 正确给出两条曲线读数差约 0.78 kN。

### Accepted Variants

- 允许读数在下述 CHART 容差内。
- 差值可写为约 0.8 kN。

### Forbidden Errors

- 交换 SWA1000-W 与 SWA2000-W 曲线。
- 把纵轴解释为标准型夹紧力。
- 直接采用 0.4 或 0.5 MPa 离散表值代替 0.45 MPa 图读数。

### Tolerance

- CHART: SWA2000-W 2.50 kN +/-0.10 kN; SWA1000-W 1.72 kN +/-0.10 kN; input pressure is exactly 0.45 MPa.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 16
- Printed page: 708
- Section: 能力曲线图（选配项 W：无下拉功能）
- Local scope path: 扩径力曲线图 > 横轴 0.45 MPa > SWA2000-W / SWA1000-W
- Evidence type: CHART
- Evidence: 曲线图分别标识两种主体尺寸的 W 型扩径力曲线；0.45 MPa 位于 0.4 和 0.5 网格线中间。

## SWA-Q-0019

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: 具有 A 工件提升功能的标准下拉型释放与夹紧动作顺序

### Question

请按动作原理图说明具有 `A` 工件提升功能的 SWA 标准下拉型从释放到夹紧
完成的气口供气和内部动作顺序，包括何时产生 0.2 mm 间隙、涨爪何时开始
下移，以及完成夹紧的判据。

### Standard Answer

释放时先向释放用供气口供气，活塞杆上升并使涨爪缩径；A 型的工件提升面
同时将工件从着座面提升 0.2 mm，形成间隙。夹紧时改向夹紧用供气口供气，
活塞杆下降，涨爪沿平面锥形部分扩径。此时起升弹簧先将涨爪举起，涨爪不
立即下移。涨爪嵌入工件后，当下拉力超过起升弹簧力，涨爪才向下移动，将
工件压紧并与着座面密接，完成夹紧。

### Scoring Standard

- P1 [15]: 正确说明释放时向释放用供气口供气。
- P2 [8]: 正确说明释放时活塞杆上升。
- P3 [7]: 正确说明释放时涨爪缩径。
- P4 [10]: 正确说明 A 型释放时产生 0.2 mm 提升间隙。
- P5 [15]: 正确说明夹紧时向夹紧用供气口供气。
- P6 [8]: 正确说明夹紧时活塞杆下降。
- P7 [7]: 正确说明涨爪沿平面锥形部分扩径。
- P8 [15]: 正确说明起升弹簧使涨爪初期不下移。
- P9 [5]: 正确说明涨爪下移的阈值是下拉力超过起升弹簧力。
- P10 [5]: 正确说明达到阈值后涨爪向下移动。
- P11 [2]: 正确说明工件最终被压紧。
- P12 [3]: 正确说明工件最终与着座面密接。

### Accepted Variants

- `起升弹簧` 可写为 `提升弹簧`。
- `密接` 可写为 `完全贴合着座面`。

### Forbidden Errors

- 在释放阶段向夹紧口供气或使涨爪扩径。
- 声称涨爪一开始扩径就立即下移。
- 省略下拉力必须超过起升弹簧力的条件。
- 将 W 无下拉型套用到本题 A 标准下拉型。

### Tolerance

- Exact 0.2 mm lift and action order are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 8
- Printed page: 700
- Section: 动作原理 > 释放状态 / 夹紧状态
- Local scope path: 状态剖面图 > 释放供气 / 活塞杆上升与缩径；夹紧供气 / 扩径 / 起升弹簧 / 下拉阈值
- Evidence type: STATE_DIAGRAM + TEXT
- Evidence: 页面按编号给出释放和夹紧动作，并将 0.2 mm 提升、起升弹簧与下拉阈值绑定到 A 标准下拉型。

## SWA-Q-0020

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: 带着座确认的标准下拉型异常检测状态

### Question

对于带着座确认的 SWA 标准下拉型，出现“释放气压 OFF、夹紧气压 ON、
着座确认 OFF”时，图中把它判为什么状态？列出 PDF 指定的四类可能原因。

### Standard Answer

该信号组合表示异常检测状态，而不是正常夹紧完成。可能原因是：工件孔径
大于可对应范围或夹紧器空动作；活塞杆或涨爪破损；活塞运行到全行程底面
限位；装卡时工件上浮 1 mm 以上。

### Scoring Standard

- P1 [30]: 正确判定信号组合为异常检测状态。
- P2 [20]: 正确列出孔径过大或空动作。
- P3 [20]: 正确列出活塞杆或涨爪破损。
- P4 [15]: 正确列出活塞全行程到底面限位。
- P5 [15]: 正确列出工件上浮 1 mm 以上。

### Accepted Variants

- `着座确认 OFF` 可写为 `空气传感器未确认密接`。
- `活塞到底` 可写为 `活塞到达全行程机械限位`。

### Forbidden Errors

- 将该组合判为正常夹紧完成；正常夹紧的着座确认应为 ON。
- 将工件上浮阈值写成 0.2 mm。
- 把 W 型无着座确认功能的常态直接套用到本题标准型。

### Tolerance

- Exact 1 mm threshold and signal states are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 8
- Printed page: 700
- Section: 动作原理 > 异常检测状态（空动作时）
- Local scope path: 异常状态剖面与信号表 > 释放 OFF / 夹紧 ON / 着座确认 OFF > 四类异常原因
- Evidence type: STATE_DIAGRAM + TEXT
- Evidence: 异常状态图将该三信号组合与孔径/空动作、破损、到底限位和 1 mm 以上上浮逐项关联。

## SWA-Q-0021

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA-N 与 VWM 组合的气压回路动作顺序和传感器配置

### Question

在 SWA-N 与 VWM 扩径定位销组合回路中，正确动作顺序是什么？若不能用
电磁阀控制顺序，应如何调整？说明顺序错误的后果，以及高精度作业时空气
传感器的配置原则。

### Standard Answer

必须先让 VWM 的定位动作结束，再使 SWA 开始夹紧动作。优先用电磁阀控制
该顺序；若不能用电磁阀，应在图示的单个指定位置设置速度控制阀等设施来
调整顺序。若 SWA 先完成而 VWM 随后动作，VWM 会对 SWA 产生推力，可能
造成机器设备损伤或定位精度不良。需要空气传感器进行高精度作业时，应为
每个夹紧器分别设置一个空气传感器。

### Scoring Standard

- P1 [25]: 正确说明 VWM 动作完成后 SWA 才开始动作。
- P2 [20]: 正确说明优先用电磁阀控制动作顺序。
- P3 [20]: 正确说明无电磁阀时在图示单个指定位置用速度控制阀调整。
- P4 [7]: 正确指出错误顺序会使 VWM 对 SWA 产生推力。
- P5 [8]: 正确指出该推力可能损伤设备。
- P6 [10]: 正确指出错误顺序可能造成定位精度不良。
- P7 [10]: 正确说明高精度作业需每个夹紧器独立空气传感器。

### Accepted Variants

- `速度控制阀` 可写为 `流量/速度调节阀`，但必须用于动作顺序调整。
- `每个夹紧器独立传感器` 可写为 `一夹紧器一传感器`。

### Forbidden Errors

- 让 SWA 先夹紧、VWM 后定位。
- 将速度控制阀放置数量写成多个任意位置。
- 多个夹紧器共用一个空气传感器并声称仍满足高精度规则。

### Tolerance

- Exact sequence direction is required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 22
- Printed page: 714
- Section: 气压回路参考范例
- Local scope path: 一/二电磁阀回路图 > 红色 VWM 必须回路；注意事项 1-2 > 顺序 / 速度控制阀 / 传感器
- Evidence type: STATE_DIAGRAM + TEXT
- Evidence: 回路页明确规定 VWM 完成后 SWA 动作，给出无电磁阀时的速度阀位置、逆序后果和逐夹紧器传感器要求。

## SWA-Q-0022

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 工件孔尺寸、勾配角、硬度和薄壁设计风险

### Question

请把以下五种工件设计偏差分别与 PDF 给出的主要后果对应：工件孔过大、
工件孔过小、工件孔过浅、锥孔勾配角过大、工件孔硬度过高。

### Standard Answer

- 孔过大：扩径量不足，夹紧力/扩径力达不到规格值。
- 孔过小：工件装卸困难，并可能使夹紧器破损。
- 孔过浅：会造成着座异常，并可能损坏气动夹紧器。
- 勾配角过大：夹紧负载集中在涨爪顶端，可能导致涨爪破损。
- 硬度过高：涨爪不能充分嵌入工件，无法充分夹紧。

### Scoring Standard

- P1 [10]: 正确对应孔过大与扩径量不足。
- P2 [10]: 正确对应孔过大与夹紧力/扩径力达不到规格值。
- P3 [10]: 正确对应孔过小与工件装卸困难。
- P4 [10]: 正确对应孔过小与夹紧器破损风险。
- P5 [10]: 正确对应孔过浅与着座异常。
- P6 [10]: 正确对应孔过浅与气动夹紧器破损风险。
- P7 [10]: 正确对应勾配角过大与负载集中在涨爪顶端。
- P8 [10]: 正确对应勾配角过大与涨爪破损风险。
- P9 [10]: 正确对应硬度过高与涨爪无法充分嵌入。
- P10 [10]: 正确对应硬度过高与夹紧不足。

### Accepted Variants

- `勾配角` 可写为 `锥度角`。
- `涨爪` 可写为 `卡爪`。

### Forbidden Errors

- 交换孔过大与孔过小的后果。
- 声称提高压力即可无条件补偿孔径、孔深、硬度或勾配角问题。

### Tolerance

- N/A

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 23
- Printed page: 715
- Section: 设计方面的注意事项 > 工件孔尺寸、勾配角和硬度
- Local scope path: 项目 6 后果表 > 五类工件孔设计偏差
- Evidence type: TEXT + DRAWING
- Evidence: 注意事项页按孔径、孔深、勾配角和硬度偏差类型逐行给出对应后果。

## SWA-Q-0023

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: 机器人搬运中的 SWA 前端插拔、坐标移动和动作联锁

### Question

请给出机器人使用 SWA 装卸工件时，防止夹紧器前端和工件损坏的完整动作
规则，包括插拔方向、退出后的坐标移动、可能接触时的插入速度、机器人与
夹紧/释放动作的联锁，以及工件与放置台间隙。

### Standard Answer

SWA 前端插入或退出工件孔时必须保持与工件孔垂直。装卸后应先让 SWA
前端完全退出工件孔，再移动到下一个坐标。若插入时可能与工件接触，应控制
插入速度以避免碰撞。应使用传感器、延迟继电器等联锁，使机器人在 SWA
夹紧或释放动作完成后才移动；动作过程中移动可能造成工件脱落。装卸时应
尽量减小工件与放置台之间的间隙，避免工件倾斜、卡滞和 SWA 损坏。

### Scoring Standard

- P1 [10]: 正确说明插入时保持 SWA 垂直于工件孔。
- P2 [10]: 正确说明退出时保持 SWA 垂直于工件孔。
- P3 [20]: 正确说明完全退出后才移动到下一坐标。
- P4 [15]: 正确说明有接触风险时控制插入速度。
- P5 [10]: 正确说明使用传感器、延迟继电器等设置动作联锁。
- P6 [10]: 正确说明夹紧或释放动作完成后机器人才能移动。
- P7 [10]: 正确说明动作中移动可能导致工件脱落。
- P8 [7]: 正确说明应尽量减小工件与放置台的间隙。
- P9 [3]: 正确说明减小间隙用于防止工件倾斜。
- P10 [3]: 正确说明减小间隙用于防止工件卡滞。
- P11 [2]: 正确说明减小间隙用于防止 SWA 损坏。

### Accepted Variants

- `延迟继电器` 可写为 `定时继电器`。
- `完全退出` 可写为 `前端完全脱离工件孔`。

### Forbidden Errors

- 允许斜向插拔或在前端仍位于孔内时平移到下一坐标。
- 允许机器人在夹紧/释放过程中继续移动。
- 建议增大工件与放置台间隙。

### Tolerance

- N/A

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 24
- Printed page: 716
- Section: 注意事项 > 机器人搬运作业中夹紧器前端部的破损防止
- Local scope path: 项目 13 > 垂直插拔 / 完全退出 / 插入速度 / 机器人联锁；装卸图 > 放置台间隙
- Evidence type: TEXT + DRAWING
- Evidence: 页面以正确/错误图和文字规定机器人插拔、坐标移动、速度、联锁与放置间隙。

## SWA-Q-0024

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 安装施工的气源、配管、密封胶带、螺栓和喷气清洁管路

### Question

请列出安装 SWA 前必须满足的气源与配管清洁要求、密封胶带缠绕规则、
本体螺栓规格和紧固力矩、喷气清洁回路的最小管径要求，并说明运行时
喷气清洁口和着座/异常确认口的供气要求。

### Standard Answer

动作流体必须是经过过滤器处理的干燥空气，不得通过油雾器供油。配管、
管接头和夹具空气通路孔在使用前必须彻底清洗，避免切屑等异物造成漏气或
动作不良。缠绕密封胶带时应在螺纹顶端留出 1-2 圈丝口，避免断头进入回路。
本体使用附带的强度等级 12.9、`M5x0.8` 螺栓，以 `6.3 N-m` 均匀紧固，
不得使机器倾斜。喷气清洁回路建议至少使用外径 phi 6 mm、内径 phi 4 mm
的管路。运行时必须始终向喷气清洁口以及着座确认/夹紧异常确认口供气；
切断这些端口的供气会使异物侵入夹紧器内部并导致动作不良。

### Scoring Standard

- P1 [10]: 正确要求过滤后的干燥空气。
- P2 [10]: 明确禁止通过油雾器供油。
- P3 [4]: 正确要求配管预先彻底清洗。
- P4 [3]: 正确要求管接头预先彻底清洗。
- P5 [3]: 正确要求夹具空气通路孔预先彻底清洗。
- P6 [15]: 正确说明密封胶带在螺纹顶端留 1-2 圈。
- P7 [8]: 正确给出 M5x0.8 螺栓规格。
- P8 [7]: 正确给出螺栓强度等级 12.9。
- P9 [8]: 正确给出紧固力矩 6.3 N-m。
- P10 [4]: 正确要求各螺栓均匀紧固。
- P11 [3]: 正确要求安装时不得使机器倾斜。
- P12 [8]: 正确给出喷气清洁管路最小外径 phi 6 mm。
- P13 [7]: 正确给出喷气清洁管路最小内径 phi 4 mm。
- P14 [5]: 正确要求喷气清洁口在运行中始终保持供气。
- P15 [5]: 正确要求着座/异常确认口在运行中始终保持供气。

### Accepted Variants

- `M5x0.8` 可写为 `M5 x 0.8`。
- `外径 phi 6、内径 phi 4` 可写为 `OD 6 mm / ID 4 mm`。

### Forbidden Errors

- 要求油雾润滑或使用未过滤湿空气。
- 将胶带一直缠到螺纹最前端。
- 使用错误力矩或省略螺栓强度等级。
- 将管径上下限方向写反。
- 允许在运行中切断喷气清洁口或着座/异常确认口的供气。

### Tolerance

- Exact 1-2 thread clearance, M5x0.8, class 12.9, 6.3 N-m, and phi 6/4 mm minimum are required.

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 23, 25
- Printed page: 715, 717
- Section: 设计方面的注意事项 / 安装施工方面的注意事项
- Local scope path: 设计注意事项项目 8 > 喷气清洁口与着座/异常确认口持续供气；安装项目 1-4 / 6 > 使用流体 / 配管前处置 / 密封胶带 / 本体安装 / 喷气清洁管路
- Evidence type: TEXT + TABLE
- Evidence: 设计注意事项要求喷气清洁口及着座/异常确认口始终供气，并说明断气会导致异物侵入和动作不良；安装页规定干燥空气、禁止供油、预清洁、胶带留牙、附带螺栓和力矩以及最小管径。

## SWA-Q-0025

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: W 无下拉型承受垂直于夹紧器轴心的横向剪切载荷

### Question

当 SWA W 无下拉型应用会受到垂直于夹紧器轴心的横向剪切载荷时，为什么
不能让夹紧器直接承受该载荷？PDF 要求采取什么设计措施？

### Standard Answer

W 型没有把工件压向着座面的下拉夹紧力，仅靠扩径力夹紧。若让它直接承受
横向剪切载荷，可能造成机器破损或工件变形。因此必须另行设置支撑，由支撑
承受该横向剪切载荷。

### Scoring Standard

- P1 [15]: 正确说明 W 型没有下拉夹紧力。
- P2 [15]: 正确说明 W 型仅靠扩径力夹紧。
- P3 [15]: 正确说明直接承受横向剪切载荷可能造成机器破损。
- P4 [15]: 正确说明直接承受横向剪切载荷可能造成工件变形。
- P5 [40]: 正确要求另设支撑来承受横向剪切载荷。

### Accepted Variants

- `横向剪切载荷` 可写为 `垂直于 SWA 轴线的侧向载荷`。
- `另设支撑` 可写为 `增加独立承载支承`。

### Forbidden Errors

- 声称 W 型的扩径力等同于下拉夹紧力。
- 允许 SWA 本体无支撑地承受全部横向剪切载荷。
- 用提高供给压力替代独立支撑。

### Tolerance

- N/A

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 4
- Printed page: 696
- Section: 特点 > 无下拉功能型的使用实例 / 注意事项
- Local scope path: W 无下拉功能型 > 翘曲方向应用 > 横向剪切载荷注意事项
- Evidence type: TEXT + DRAWING
- Evidence: 页面说明 W 型无夹紧力，横向剪切载荷会导致机器破损或工件变形，并要求另设支撑承载。

## SWA-Q-0026

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 日常清扫、故障判断和分解大修边界

### Question

请说明 SWA 日常清扫与装卡前检查要求、带污运行的后果，以及外部清扫后
仍不能正常动作时应如何判断和处理。

### Standard Answer

应定期清扫夹紧部位和着座面，并在装卡前确认没有切屑、淤渣等异物堆积。
带污运行会造成夹紧力不足、动作异常和漏气，可能导致工件脱落。外部清扫后
仍不能正常动作时，应怀疑内部混入异物或元件损坏，并委托 KOSMEK 分解大修，
不得自行拆解，因为产品内置强劲弹簧。

### Scoring Standard

- P1 [10]: 正确要求定期清扫夹紧部位。
- P2 [10]: 正确要求定期清扫着座面。
- P3 [10]: 正确要求装卡前确认无异物。
- P4 [15]: 正确说明带污会导致夹紧力不足。
- P5 [10]: 正确说明带污会导致动作异常。
- P6 [10]: 正确说明带污会导致漏气。
- P7 [10]: 正确说明带污运行存在工件脱落风险。
- P8 [5]: 正确说明外部清扫无效时怀疑内部混入异物。
- P9 [5]: 正确说明外部清扫无效时怀疑内部元件损坏。
- P10 [10]: 正确要求委托 KOSMEK 分解大修。
- P11 [5]: 正确说明内置强弹簧，因此不得自行拆解。

### Accepted Variants

- `KOSMEK` 可写为 `制造商` 或 `本公司`。
- `确认回路压力为零` 可写为 `泄压到零`。

### Forbidden Errors

- 仅依赖喷气清洁而不做定期人工检查。
- 外部清扫无效后继续运行或自行拆解。

### Tolerance

- N/A

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 26
- Printed page: 718
- Section: 保养・检查
- Local scope path: SWA 保养项目 2/4 > 清扫 / 异常 / 制造商分解大修 / 强弹簧警告
- Evidence type: TEXT
- Evidence: SWA 本地保养页规定清扫、污染后果、异常判断和制造商分解大修，并警告产品内置强劲弹簧，不得自行拆解。

## SWA-Q-0027

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 操作、拆卸和重新启动安全

### Question

SWA 的操作、拆卸和重新启动必须采取哪些人员、设备运动、能源隔离、温度、
夹伤和改造方面的安全措施？

### Standard Answer

操作人员必须经过充分培训并具备相应知识。拆卸前必须采取防止工件或设备
坠落以及防止设备误动作的措施，切断压力源和电源，并确认回路压力为零。
设备完全冷却后才可拆卸。重新启动前必须检查螺栓和连接部位是否异常。
运行中不得接近或触碰夹紧器，避免夹伤；不得擅自改造产品。

### Scoring Standard

- P1 [15]: 正确要求操作人员经过培训并具备相应知识。
- P2 [10]: 正确要求拆卸前采取防坠落措施。
- P3 [10]: 正确要求拆卸前采取防误动作措施。
- P4 [10]: 正确要求切断压力源。
- P5 [10]: 正确要求切断电源。
- P6 [10]: 正确要求确认回路压力为零。
- P7 [10]: 正确要求设备完全冷却后再拆卸。
- P8 [5]: 正确要求重启前检查螺栓。
- P9 [5]: 正确要求重启前检查连接部位。
- P10 [5]: 正确要求运行中避免接近或触碰夹紧器以防夹伤。
- P11 [10]: 正确要求不得擅自改造产品。

### Accepted Variants

- `确认回路压力为零` 可写为 `泄压到零`。
- `防误动作` 可写为 `防止设备意外启动或移动`。

### Forbidden Errors

- 只切断电源而保留气压，或未确认回路压力为零。
- 未采取防坠落、防误动作措施便拆卸。
- 在设备尚未冷却时拆卸。
- 允许未培训人员操作或允许擅自改造产品。

### Tolerance

- N/A

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 25
- Printed page: 717
- Section: 操作方面的注意事项
- Local scope path: 操作安全项目 1-5 > 人员资格 / 防坠落与防误动作 / 零能量 / 冷却 / 重启检查 / 夹伤 / 禁止改造
- Evidence type: TEXT
- Evidence: SWA 产品本地操作注意事项逐项规定人员资格、防坠落、防误动作、压力与电源隔离、零压力确认、冷却、重启检查、夹伤防止和禁止改造。

## SWA-Q-0028

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: SWA 气动涨紧下拉夹紧器
- Model / Scope: SWA 工件孔周边薄壁条件的试夹与压力调整

### Question

当 SWA 对象工件的孔周边存在薄壁部位时，夹紧会产生什么风险？投入使用前
必须执行什么验证和调整，若夹紧力或扩径力不足会造成什么后果？

### Standard Answer

孔周边为薄壁时，夹紧动作可能使工件孔变形，并使夹紧力或扩径力达不到
规定值。投入使用前必须进行夹紧试验，并把供给气压调整到最合适的夹紧
状态。若在夹紧力或扩径力不足的状态下使用，可能发生工件脱落事故。

### Scoring Standard

- P1 [20]: 正确说明薄壁条件可能使工件孔变形。
- P2 [20]: 正确说明薄壁条件可能使夹紧力或扩径力达不到规定值。
- P3 [20]: 正确要求投入使用前进行夹紧试验。
- P4 [20]: 正确要求依据试夹结果调整供给气压到合适状态。
- P5 [20]: 正确说明力不足时存在工件脱落风险。

### Accepted Variants

- `夹紧试验` 可写为 `试夹`。
- `供给气压调整到合适状态` 可写为 `根据试夹结果优化工作压力`。

### Forbidden Errors

- 省略试夹验证并直接投入运行。
- 声称提高压力即可无条件消除薄壁变形。
- 声称夹紧力或扩径力不足不会导致工件脱落。

### Tolerance

- N/A

### Source

- PDF: SWA_R00_FA2026-C1N.pdf
- Physical page: 23
- Printed page: 715
- Section: 设计方面的注意事项 > 工件孔周边壁厚
- Local scope path: 项目 7 > 薄壁变形 / 夹紧力与扩径力不足 / 夹紧试验 / 供给气压调整 / 脱落风险
- Evidence type: TEXT + DRAWING
- Evidence: 薄壁注意事项明确关联孔变形、力不足、试夹、压力调整和工件脱落风险。
