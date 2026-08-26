---
schema_version: will-ai-question-bank/v1
source_pdf: VFLVFM_R00_2023KW_C1N.pdf
source_sha256: 711dfc7c3a7573f3e4da94a0c2c4ee99ea6aefe26fdf41c1722884ab671b8e2b
source_pages: 52
question_bank_version: V1
product_scope: VFL / VFM
---

# VFLVFM_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `VFLVFM_R00_2023KW_C1N.pdf`
- SHA-256: `711dfc7c3a7573f3e4da94a0c2c4ee99ea6aefe26fdf41c1722884ab671b8e2b`
- Physical pages: 52
- Product scope: VFL 弹簧定位/油压释放型与 VFM 油压定位/油压释放型扩径定位销，以及 PDF 内直接适用的设计、安装、回路、操作和维护要求

## 2. Scope

本题库把 VFL 与 VFM 作为同一份组合来源中的两个产品范围，覆盖型号语法、动作原理、D/C 定位功能、规格与能力、可定位工件重量计算、剪切载荷/变位曲线、选配检测、安装相位、配管回路和直接适用的共通注意事项。公司介绍、销售网点、纯目录导航以及 VFH/VFLJ/VFJ/VFK 等其他系列的专属规格不作为考核对象。

### 2.1 覆盖原则

- `HIGH`：型号、动作、能力、精度、检测、相位、安装、回路和故障后果均映射到题目。
- `MEDIUM`：直接适用于 VFL/VFM 的液压施工、操作与维护要求映射到代表题。
- `LOW/EXCLUDED`：纯导航、重复语言页、公司与销售资料及其他系列专属数据保留处置理由，不生成题目。

### 2.2 图表与计算边界

- 离散规格使用 `TABLE`；连续剪切载荷/变位曲线使用 `CHART`，Gold 来自物理页 26 的视觉读图，不以表值或公式替代。
- 可定位工件重量与孔间距误差预算使用 PDF 公式和明确输入作确定性计算；最终值采用 `ROUND_HALF_UP`。

### 2.3 来源清单

| Coverage ID | 物理页 | 局部范围 | Evidence type | 可测试对象 / 范围决定 | Priority / Disposition |
|---|---:|---|---|---|---|
| VFLVFM-SI-001 | 1-2 | 产品总览与系列比较 | TEXT + TABLE | 重复定位精度、压力类型、清洁和检测选配；`VFLVFM-Q-0003`、`0005`、`0012` | HIGH：已映射 |
| VFLVFM-SI-002 | 3-4 | VFL/VFM 动作原理 | STATE_DIAGRAM + TEXT | 两系列定位与释放顺序；`VFLVFM-Q-0003`-`0004` | HIGH：已映射 |
| VFLVFM-SI-003 | 5-6 | 系统参考范例 | DRAWING + CAUTION | D/C 功能、孔精度、独立夹紧和相位；`VFLVFM-Q-0010`-`0011` | HIGH：已映射 |
| VFLVFM-SI-004 | 7-8 | VFL 型号表示 | MODEL + TABLE | VFL 字段与组合；`VFLVFM-Q-0001` | HIGH：已映射 |
| VFLVFM-SI-005 | 9-10 | VFL 规格与能力曲线 | TABLE + FORMULA + CHART | VFL 能力和共通规格；`VFLVFM-Q-0005`-`0006` | HIGH：已映射 |
| VFLVFM-SI-006 | 11-22 | VFL 标准/B/M 外形尺寸 | DRAWING + TABLE + CAUTION | 检测、安装密封与端口；`VFLVFM-Q-0012`-`0014` | HIGH：已映射 |
| VFLVFM-SI-007 | 23-24 | VFM 型号表示 | MODEL + TABLE | VFM 字段与组合；`VFLVFM-Q-0002` | HIGH：已映射 |
| VFLVFM-SI-008 | 25-26 | VFM 规格、重量公式和能力曲线 | TABLE + FORMULA + CHART | 压力相关扩径力、重量计算与视觉变位；`VFLVFM-Q-0007`-`0009` | HIGH：已映射 |
| VFLVFM-SI-009 | 27-38 | VFM 标准/B/M 外形尺寸 | DRAWING + TABLE + CAUTION | 安装与检测选配边界；`VFLVFM-Q-0012`-`0014` | HIGH：已映射 |
| VFLVFM-SI-010 | 39-40 | 扩径定位销设计注意事项 | CAUTION + DRAWING | 连续供气、相位、倾斜和薄壁孔；`VFLVFM-Q-0011`、`0013`、`0015`、`0018` | HIGH：已映射 |
| VFLVFM-SI-011 | 41-42 | VFL/VFM 安装施工与间距精度 | TABLE + FORMULA + PROCEDURE | 力矩、O 形圈、排气口和误差预算；`VFLVFM-Q-0014`、`0017`、`0019` | HIGH：已映射 |
| VFLVFM-SI-012 | 43-44 | VFL/VFM 参考回路 | PROCEDURE + CAUTION | 动作顺序、背压与脉冲高压；`VFLVFM-Q-0016` | HIGH：已映射 |
| VFLVFM-SI-013 | 45-48 | 液压系列通用施工、操作与维护 | PROCEDURE + CAUTION | 清洁、排气、定检和安全边界；`VFLVFM-Q-0020` | MEDIUM：已映射 |
| VFLVFM-SI-014 | 49-50 | 标示变更与通用附录 | TABLE + TEXT | 重复标准资料 | LOW：不构成 VFL/VFM 耐久产品题 |
| VFLVFM-SI-015 | 51-52 | 公司与销售网点 | TEXT | 联系方式与公司信息 | EXCLUDED：非耐久技术知识 |

## 3. Question Statistics

- Total: 20
- Direct VFL/VFM: 19
- Document Common: 1
- MODEL: 2
- FACT: 2
- SPEC_LOOKUP: 2
- TABLE: 2
- CALCULATION: 2
- CHART: 1
- PROCEDURE: 4
- CAUTION: 5

## 4. Questions

## VFLVFM-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: VFL 扩径定位销
- Model / Scope: `VFL2000-080-D-H20-MR`

### Question

逐段解释型号 `VFL2000-080-D-H20-MR` 中的系列、主体尺寸、设计编号、工件孔径符号、功能、着座高度、选配项和供气口位置。

### Standard Answer

`VFL` 表示弹簧定位、油压释放的扩径定位销；`2` 表示主体尺寸 2，适用于 φ8～φ11 工件孔；`000` 中的设计编号为 0；`080` 表示 φ8H8 工件孔；`D` 是基准定位用基准销；`H20` 表示着座高度 20 mm；`M` 是释放动作确认型；`R` 表示供气口采用外形尺寸页所示的 R 位置。

### Scoring Standard

- P1 [10]: `VFL` 正确识别为扩径定位销系列。
- P2 [10]: `VFL` 的定位动力正确写为弹簧力。
- P3 [10]: `VFL` 的释放动力正确写为油压。
- P4 [10]: 主体尺寸 `2` 正确对应 φ8～φ11 工件孔。
- P5 [10]: 设计编号正确写为 `0`。
- P6 [10]: `080` 正确对应 φ8H8 工件孔。
- P7 [10]: `D` 正确解释为基准定位用基准销。
- P8 [10]: `H20` 正确解释为 20 mm 着座高度。
- P9 [10]: `M` 正确解释为释放动作确认型。
- P10 [10]: `R` 正确解释为供气口 R 位置。

### Accepted Variants

- “圆销定位”可作为 D 基准销功能的补充说法，但不能替代基准定位含义。

### Forbidden Errors

- 将 VFL 说成油压定位，或将 M 说成着座确认型。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1331-1332
- Section: VFL 型号表示
- Local scope path: VFL > 型号表示 > 字段 1 至 7
- Evidence type: MODEL
- Evidence: 型号示例及字段表逐项定义系列、主体尺寸、孔径、D/C、H 高度、B/M 和 R/L。

## VFLVFM-Q-0002

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: VFM 扩径定位销
- Model / Scope: `VFM6000-300-C-H30-BL`

### Question

逐段解释型号 `VFM6000-300-C-H30-BL` 中的系列、主体尺寸、设计编号、工件孔径符号、功能、着座高度、选配项和供气口位置。

### Standard Answer

`VFM` 表示油压定位、油压释放的复动型扩径定位销；`6` 表示主体尺寸 6，适用于 φ26～φ30 工件孔；设计编号为 0；`300` 表示 φ30H8 工件孔；`C` 是单一方向定位用菱形销；`H30` 表示着座高度 30 mm；`B` 是着座确认型；`L` 表示供气口采用外形尺寸页所示的 L 位置。

### Scoring Standard

- P1 [10]: `VFM` 正确识别为扩径定位销系列。
- P2 [10]: `VFM` 的定位动力正确写为油压。
- P3 [10]: `VFM` 的释放动力正确写为油压。
- P4 [10]: 主体尺寸 `6` 正确对应 φ26～φ30 工件孔。
- P5 [10]: 设计编号正确写为 `0`。
- P6 [10]: `300` 正确对应 φ30H8 工件孔。
- P7 [10]: `C` 正确解释为单一方向定位用菱形销。
- P8 [10]: `H30` 正确解释为 30 mm 着座高度。
- P9 [10]: `B` 正确解释为着座确认型。
- P10 [10]: `L` 正确解释为供气口 L 位置。

### Accepted Variants

- “切边销”可作为 C 菱形销的同义说法。

### Forbidden Errors

- 将 VFM 说成弹簧定位，或将 B 说成释放动作确认型。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 23
- Printed page: 1345-1346
- Section: VFM 型号表示
- Local scope path: VFM > 型号表示 > 字段 1 至 7
- Evidence type: MODEL
- Evidence: VFM 型号示例、主体尺寸/孔径表和选配项定义共同给出各字段含义。

## VFLVFM-Q-0003

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 两系列驱动方式比较

### Question

VFL 与 VFM 分别采用什么定位和释放方式？各自属于油压单动型还是油压复动型？

### Standard Answer

VFL 由弹簧力定位、油压释放，属于油压单动型；VFM 由油压定位、油压释放，属于油压复动型。

### Scoring Standard

- P1 [17]: VFL 正确写为弹簧力定位。
- P2 [17]: VFL 正确写为油压释放。
- P3 [16]: VFL 正确归类为油压单动型。
- P4 [17]: VFM 正确写为油压定位。
- P5 [17]: VFM 正确写为油压释放。
- P6 [16]: VFM 正确归类为油压复动型。

### Accepted Variants

- “弹簧定位”与“弹簧力定位”等价。

### Forbidden Errors

- 声称 VFL 的定位需要持续定位油压，或把 VFM 归为单动型。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 3
- Printed page: 1327-1328
- Section: 动作原理
- Local scope path: VFL/VFM > 动作原理 > 定位与释放驱动
- Evidence type: STATE_DIAGRAM
- Evidence: 两套动作图分别标注 VFL 的弹簧定位/油压释放和 VFM 的油压定位/油压释放。

## VFLVFM-Q-0004

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 定位与释放动作顺序

### Question

分别说明 VFL 与 VFM 从定位状态切换到释放状态、再恢复定位时的压力操作和内部动作。

### Standard Answer

VFL 释放时供给释放油压，使活塞和活塞杆上升并推动锥套，锥套靠弹性复原缩径；撤除释放油压后，弹簧使活塞和活塞杆下降，锥套扩径并恢复定位。VFM 释放时先撤除定位油压并供给释放油压，使活塞和活塞杆上升、锥套缩径；恢复定位时撤除释放油压并供给定位油压，使活塞和活塞杆下降、锥套扩径。

### Scoring Standard

- P1 [8]: VFL 释放时供给释放油压。
- P2 [8]: VFL 释放时活塞和活塞杆上升。
- P3 [7]: VFL 释放时锥套缩径。
- P4 [7]: VFL 恢复定位前撤除释放油压。
- P5 [7]: VFL 恢复定位时弹簧使活塞和活塞杆下降。
- P6 [7]: VFL 恢复定位时锥套扩径。
- P7 [7]: VFM 释放前撤除定位油压。
- P8 [7]: VFM 释放时供给释放油压。
- P9 [7]: VFM 释放时活塞和活塞杆上升。
- P10 [7]: VFM 释放时锥套缩径。
- P11 [7]: VFM 恢复定位前撤除释放油压。
- P12 [7]: VFM 恢复定位时供给定位油压。
- P13 [7]: VFM 恢复定位时活塞和活塞杆下降。
- P14 [7]: VFM 恢复定位时锥套扩径。

### Accepted Variants

- 可将“锥套”写作“扩径套”，前提是动作方向完整正确。

### Forbidden Errors

- 同时向 VFM 的定位侧和释放侧供压作为正常切换方法。

### Tolerance

- 步骤顺序必须正确。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 3
- Printed page: 1327-1328
- Section: 动作原理
- Local scope path: VFL/VFM > 动作原理 > 释放状态与定位状态
- Evidence type: STATE_DIAGRAM
- Evidence: 动作图以箭头和说明列出供压、撤压、活塞杆方向与锥套扩缩顺序。

## VFLVFM-Q-0005

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 两系列共通使用条件

### Question

VFL/VFM 的重复定位精度、使用压力范围、耐压、推荐喷气清洁用气压、使用温度范围和规定使用流体分别是什么？

### Standard Answer

重复定位精度为 3 μm；使用压力范围为 2.5～7.0 MPa；耐压为 10.5 MPa；推荐喷气清洁用气压为 0.3～0.4 MPa；使用温度范围为 0～70 ℃；使用流体为相当于 ISO 粘度等级 ISO-VG-32 的一般液压油。

### Scoring Standard

- P1 [17]: 重复定位精度为 3 μm。
- P2 [17]: 使用压力范围为 2.5～7.0 MPa。
- P3 [17]: 耐压为 10.5 MPa。
- P4 [17]: 推荐喷气清洁用气压为 0.3～0.4 MPa。
- P5 [16]: 使用温度范围为 0～70 ℃。
- P6 [16]: 使用流体为相当于 ISO-VG-32 的一般液压油。

### Accepted Variants

- `ISO VG 32` 与 `ISO-VG-32` 等价；3 μm 可写作 0.003 mm。

### Forbidden Errors

- 将 10.5 MPa 当作连续使用压力上限。

### Tolerance

- 数值与范围按表值精确判定。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 9 and 25
- Printed page: 1333-1334 and 1347-1348
- Section: VFL 规格 / VFM 规格
- Local scope path: VFL > 规格 > 共通使用条件；VFM > 规格 > 共通使用条件
- Evidence type: TABLE
- Evidence: 物理页 9 的 VFL2000～VFL6000 规格表与物理页 25 的 VFM2000～VFM6000 规格表分别直接给出相同的 3 μm、2.5～7.0 MPa、10.5 MPa、0.3～0.4 MPa、0～70 ℃和 ISO-VG-32 条件。

## VFLVFM-Q-0006

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: VFL 扩径定位销
- Model / Scope: VFL2000/VFL4000/VFL6000 代表规格

### Question

写出 `VFL2000-100`、`VFL4000-200`、`VFL6000-300` 的标准孔径、扩径力和容许剪切载荷。

### Standard Answer

`VFL2000-100`：φ10H8、220 N、2000 N；`VFL4000-200`：φ20H8、290 N、4000 N；`VFL6000-300`：φ30H8、1080 N、9000 N。

### Scoring Standard

- P1 [12]: `VFL2000-100` 标准孔径为 φ10H8。
- P2 [11]: `VFL2000-100` 扩径力为 220 N。
- P3 [11]: `VFL2000-100` 容许剪切载荷为 2000 N。
- P4 [11]: `VFL4000-200` 标准孔径为 φ20H8。
- P5 [11]: `VFL4000-200` 扩径力为 290 N。
- P6 [11]: `VFL4000-200` 容许剪切载荷为 4000 N。
- P7 [11]: `VFL6000-300` 标准孔径为 φ30H8。
- P8 [11]: `VFL6000-300` 扩径力为 1080 N。
- P9 [11]: `VFL6000-300` 容许剪切载荷为 9000 N。

### Accepted Variants

- 孔径可写作“φ10 H8”等带空格形式。

### Forbidden Errors

- 把 VFM 在某一压力下的扩径力当作 VFL 的弹簧扩径力。

### Tolerance

- 表值精确判定。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 1333-1334
- Section: VFL 规格
- Local scope path: VFL > 规格 > 孔径符号、扩径力与容许剪切载荷
- Evidence type: TABLE
- Evidence: VFL2000～VFL6000 规格表逐行给出标准孔径、扩径力和容许剪切载荷。

## VFLVFM-Q-0007

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: VFM 扩径定位销
- Model / Scope: VFM2000/VFM4000/VFM6000 在 5.0 MPa 时的代表规格

### Question

在定位压力 5.0 MPa 时，写出 `VFM2000-100`、`VFM4000-200`、`VFM6000-300` 的扩径力，并写出各自容许剪切载荷。

### Standard Answer

`VFM2000-100`：扩径力 700 N、容许剪切载荷 2000 N；`VFM4000-200`：扩径力 1000 N、容许剪切载荷 4000 N；`VFM6000-300`：扩径力 2630 N、容许剪切载荷 9000 N。

### Scoring Standard

- P1 [17]: `VFM2000-100` 在 5.0 MPa 时扩径力为 700 N。
- P2 [17]: `VFM2000-100` 容许剪切载荷为 2000 N。
- P3 [17]: `VFM4000-200` 在 5.0 MPa 时扩径力为 1000 N。
- P4 [17]: `VFM4000-200` 容许剪切载荷为 4000 N。
- P5 [16]: `VFM6000-300` 在 5.0 MPa 时扩径力为 2630 N。
- P6 [16]: `VFM6000-300` 容许剪切载荷为 9000 N。

### Accepted Variants

- 允许使用千牛表示：0.7 kN、1.0 kN、2.63 kN，以及 2、4、9 kN。

### Forbidden Errors

- 使用 2.5 MPa 或 7.0 MPa 列中的扩径力。

### Tolerance

- 表值精确判定。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1347-1348
- Section: VFM 规格
- Local scope path: VFM > 规格 > 5.0 MPa 扩径力与容许剪切载荷
- Evidence type: TABLE
- Evidence: VFM 两组规格表按 2.5、5.0、7.0 MPa 分列扩径力，并逐行给出容许剪切载荷。

## VFLVFM-Q-0008

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: VFM 扩径定位销
- Model / Scope: `VFM2000-100` 在 5.0 MPa 时的可定位工件重量

### Question

`VFM2000-100` 在 5.0 MPa 时扩径力 F=700 N。按 PDF 的效率 0.5，工件着座面摩擦系数 μ=0.2，分别计算水平平置和垂直挂壁装卡时的最大可定位工件重量。结果保留 1 位小数。

### Standard Answer

水平平置：`W ≤ F×0.5/(μ×9.8) = 700×0.5/(0.2×9.8) = 178.571... kg`，按 `ROUND_HALF_UP` 得 **178.6 kg**。垂直挂壁：`W ≤ F×0.5/9.8 = 700×0.5/9.8 = 35.714... kg`，按 `ROUND_HALF_UP` 得 **35.7 kg**。

### Scoring Standard

- P1 [15]: 水平姿势采用 `F×0.5/(μ×9.8)`。
- P2 [10]: 水平姿势正确代入 F=700 N。
- P3 [10]: 水平姿势正确代入 μ=0.2。
- P4 [15]: 水平姿势未舍入值为 178.571... kg。
- P5 [15]: 水平姿势最终 Gold 为 178.6 kg。
- P6 [10]: 垂直姿势采用 `F×0.5/9.8`。
- P7 [10]: 垂直姿势未舍入值为 35.714... kg。
- P8 [15]: 垂直姿势最终 Gold 为 35.7 kg。

### Accepted Variants

- 中间值可保留更多小数；最终值必须按 `ROUND_HALF_UP` 保留 1 位小数。

### Forbidden Errors

- 在垂直姿势公式中再次除以摩擦系数，或漏用效率 0.5。

### Tolerance

- 使用 `ROUND_HALF_UP` 精确舍入到 1 位小数：水平必须为 178.6 kg，垂直必须为 35.7 kg；不另设正负容差。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1347-1348
- Section: 扩径力与可定位工件重量的关系式
- Local scope path: VFM > 规格 > 水平姿势与垂直姿势公式
- Evidence type: FORMULA
- Evidence: 公式图分别给出水平和垂直装卡的重量上限、效率 0.5、摩擦系数与重力换算关系。

## VFLVFM-Q-0009

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: VFM 扩径定位销
- Model / Scope: `VFM6000-300` 剪切载荷/变位曲线

### Question

仅依据物理页 26 的 `VFM6000` 剪切载荷/变位曲线，视觉读取扩径状态下 `VFM6000-300` 承受 8000 N 静态剪切载荷时的变位约为多少？

### Standard Answer

在 `VFM6000` 图中沿横轴 8000 N 向上读取 `VFM6000-300` 曲线，再向纵轴投影，变位约为 **0.014 mm**。

### Scoring Standard

- P1 [25]: 使用的是 `VFM6000` 曲线组。
- P2 [25]: 选择的是 `VFM6000-300` 曲线。
- P3 [25]: 在横轴 8000 N 位置进行视觉读取。
- P4 [25]: 读图结果落在 0.012～0.016 mm。

### Accepted Variants

- 0.012～0.016 mm 内的视觉估读均接受。

### Forbidden Errors

- 用容许剪切载荷表值 9000 N 代替变位，或引用页面示例 `VFM2000-100` 的 0.018 mm。

### Tolerance

- Gold: 0.014 mm；接受范围 0.012～0.016 mm。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 1347-1348
- Section: 剪切载荷/变位曲线图
- Local scope path: VFM > 规格 > VFM6000 曲线组 > VFM6000-300
- Evidence type: CHART
- Evidence: 连续曲线以剪切载荷为横轴、变位为纵轴，VFM6000-300 是该曲线组中独立标注的曲线。

## VFLVFM-Q-0010

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: D/C 定位功能与基本边界

### Question

说明 D 与 C 两种功能的定位职责，并说明扩径状态、释放状态和夹紧功能的边界。

### Standard Answer

D 是基准定位用基准销，相当于圆销；C 是单一方向定位用菱形销，相当于切边销。扩径状态通过与工件基准孔实现零间隙来定位；释放状态保留足够间隙以便装卸。VFL/VFM 仅用于定位，不具备夹紧功能，必须另设夹紧器。

### Scoring Standard

- P1 [17]: D 正确解释为基准定位用基准销。
- P2 [17]: C 正确解释为单一方向定位用菱形销。
- P3 [17]: 扩径状态与工件基准孔实现零间隙定位。
- P4 [17]: 释放状态保留装卸所需间隙。
- P5 [16]: VFL/VFM 不具备夹紧功能。
- P6 [16]: 必须另设夹紧器。

### Accepted Variants

- D 可称圆销，C 可称切边销或钻石销。

### Forbidden Errors

- 声称扩径定位销能够替代工件夹紧器。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 1329-1330
- Section: 系统参考范例
- Local scope path: VFL/VFM > 系统参考范例 > 基准销、菱形销和着座
- Evidence type: DRAWING
- Evidence: 系统图标注 D/C 职责、扩径/释放间隙，并明确定位销没有夹紧功能。

## VFLVFM-Q-0011

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: C 菱形销相位与安装孔间距

### Question

VFL/VFM 的 C 菱形销相对于 D 基准销应如何定相？定位销安装孔的间距精度要求是多少？相位或间距不正确有什么风险？

### Standard Answer

C 菱形销的扩径方向必须与 C、D 两销中心连线垂直，并应以外观上的定位方向标记确认相位；VFL/VFM 安装孔间距精度应控制在 ±0.02 mm 以内。相位错误会破坏单一方向定位关系，间距误差超出容许偏心预算会造成不能正确定位、精度不良或零件损伤。

### Scoring Standard

- P1 [20]: C 的扩径方向与 C、D 中心连线垂直。
- P2 [20]: 安装时使用定位方向标记确认相位。
- P3 [20]: 安装孔间距精度为 ±0.02 mm 以内。
- P4 [20]: 相位错误会破坏单一方向定位关系。
- P5 [20]: 超出误差预算会破坏正确定位关系。

### Accepted Variants

- “中心连线成 90°”等同于“垂直”。

### Forbidden Errors

- 将 C 的扩径方向沿着 C、D 中心连线安装。

### Tolerance

- ±0.02 mm 按原文精确判定。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 1395-1396
- Section: 关于定位销的安装方向（相位）
- Local scope path: 扩径定位销注意事项 > 设计 > C/D 相位
- Evidence type: CAUTION
- Evidence: 相位示意图给出垂直关系、方向标记和 ±0.02 mm 安装孔间距要求。

## VFLVFM-Q-0012

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 标准、B、M 选配及 Z 轴着座

### Question

无符号标准型、B 型和 M 型分别提供什么检测功能？哪些类型自带 Z 轴着座，哪些必须另设着座？B 与 M 组合时如何处理？

### Standard Answer

无符号是无检测选配的标准型；B 是着座确认型，并在法兰上面设置 Z 轴着座；M 是释放动作确认型。标准型与 M 型没有 Z 轴方向基准着座，必须另设定位着座面。B 与 M 如需组合使用，必须另行咨询，不能当作普通标准组合直接选用。

### Scoring Standard

- P1 [15]: 无符号正确解释为无检测选配的标准型。
- P2 [15]: B 正确解释为着座确认型。
- P3 [14]: B 型法兰上面带有 Z 轴着座。
- P4 [14]: M 正确解释为释放动作确认型。
- P5 [14]: 标准型必须另设 Z 轴定位着座面。
- P6 [14]: M 型必须另设 Z 轴定位着座面。
- P7 [14]: B 与 M 组合必须另行咨询。

### Accepted Variants

- “落座确认”可等同于“着座确认”。

### Forbidden Errors

- 声称 M 型自带工件着座面，或允许 B/M 无条件组合。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 23
- Printed page: 1345-1346
- Section: VFM 型号表示与选配项
- Local scope path: VFM > 型号表示 > 选配项和着座注意事项
- Evidence type: TABLE
- Evidence: 选配表定义无符号/B/M，注意事项说明标准/M 另设着座及 B/M 组合需咨询。

## VFLVFM-Q-0013

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 喷气清洁与检测端口连续供气

### Question

运行 VFL/VFM 时，喷气清洁、B 型着座确认和 M 型释放确认三个空气端口应如何供气？切断喷气清洁供气继续使用会有什么后果？

### Standard Answer

空气清洁用供气口应始终保持供气；B 型还应始终向着座确认用供气口供气；M 型还应始终向释放动作确认用供气口供气。若切断空气清洁供气后继续使用，冷却液、切削屑等异物会侵入装置内部，导致定位销动作异常。

### Scoring Standard

- P1 [20]: 空气清洁用供气口始终供气。
- P2 [20]: B 型着座确认用供气口始终供气。
- P3 [20]: M 型释放动作确认用供气口始终供气。
- P4 [20]: 切断清洁供气会让异物侵入装置内部。
- P5 [20]: 异物侵入会导致定位销动作异常。

### Accepted Variants

- “连续供气”与“始终供气”等价。

### Forbidden Errors

- 仅在动作切换瞬间向空气清洁口供气。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 1395-1396
- Section: 关于供气
- Local scope path: 扩径定位销注意事项 > 设计 > 连续供气
- Evidence type: PROCEDURE
- Evidence: 供气注意事项逐项要求清洁口、B 检测口和 M 检测口始终供气并列出断气后果。

## VFLVFM-Q-0014

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 本体安装、O 形圈与紧固力矩

### Question

安装 VFL/VFM 本体时，随附 O 形圈和安装螺栓应如何处理？分别给出主体尺寸 2/3、4/5、6 的螺栓规格与紧固力矩，并说明禁止使用的垫圈。

### Standard Answer

应先把随附 O 形圈装到夹具侧安装孔，再装本体；使用随附强度等级 12.9 的内六角螺栓并均匀紧固。主体尺寸 2/3 使用 M5×0.8、6.3 N·m；尺寸 4/5 使用 M6、10 N·m；尺寸 6 使用 M8、25 N·m。不得使用弹簧垫圈或带齿垫圈。

### Scoring Standard

- P1 [10]: 先将随附 O 形圈装到夹具侧安装孔。
- P2 [10]: 使用强度等级 12.9 的随附内六角螺栓。
- P3 [10]: 螺栓应均匀紧固。
- P4 [10]: 主体尺寸 2/3 的螺栓规格为 M5×0.8。
- P5 [10]: 主体尺寸 2/3 的紧固力矩为 6.3 N·m。
- P6 [10]: 主体尺寸 4/5 的螺栓规格为 M6。
- P7 [10]: 主体尺寸 4/5 的紧固力矩为 10 N·m。
- P8 [10]: 主体尺寸 6 的螺栓规格为 M8。
- P9 [10]: 主体尺寸 6 的紧固力矩为 25 N·m。
- P10 [5]: 禁止使用弹簧垫圈。
- P11 [5]: 禁止使用带齿垫圈。

### Accepted Variants

- `N·m` 可写作 `Nm`；M5×0.8 可写作 M5 螺距 0.8。

### Forbidden Errors

- 先装本体再把 O 形圈从上方塞入，或任意提高紧固力矩。

### Tolerance

- 螺栓规格与力矩按表值精确判定。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 41
- Printed page: 1397-1398
- Section: 机器的安装·拆卸 / O 形密封圈安装
- Local scope path: VFL/VFM 注意事项 > 安装施工 > O 形圈和力矩表
- Evidence type: TABLE
- Evidence: 安装注意事项规定 O 形圈先装夹具侧、12.9 级螺栓、均匀紧固、禁用垫圈，并按型号给出力矩。

## VFLVFM-Q-0015

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 倾斜装卸与垂直挂壁使用

### Question

工件倾斜装卸和垂直挂壁使用 VFL/VFM 时，应遵守哪些限制与保护措施？

### Standard Answer

工件与定位销的倾斜度应控制在 4/100～5/100（约 2～3°）以内；搬入搬出尤其是搬出时应设置导向销（粗导销），避免扩径部与孔卡滞。垂直装卡时不得让工件浮起或倾斜；释放时应设外部预夹紧装置防止工件掉落；还应定期确认定位精度，超出容许范围立即更换定位销。

### Scoring Standard

- P1 [14]: 倾斜度控制在 4/100～5/100 以内。
- P2 [14]: 该倾斜范围约为 2～3°。
- P3 [14]: 装卸时设置导向销或粗导销。
- P4 [14]: 垂直装卡时避免工件浮起或倾斜。
- P5 [14]: 释放时设置外部预夹紧装置防掉落。
- P6 [15]: 垂直使用时定期确认定位精度。
- P7 [15]: 定位精度超出容许范围时立即更换定位销。

### Accepted Variants

- 4%～5% 可作为 4/100～5/100 的等价表达。

### Forbidden Errors

- 允许工件倾斜装卸而不设置任何导向或防落措施。

### Tolerance

- 角度和比值范围按原文判定。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 1395-1396
- Section: Z 轴方向倾斜度 / 垂直姿势使用
- Local scope path: 扩径定位销注意事项 > 设计 > 倾斜装卸与挂壁
- Evidence type: CAUTION
- Evidence: 注意事项给出倾斜比、近似角度、导向销、预夹紧和定期精度确认要求。

## VFLVFM-Q-0016

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 定位夹紧顺序与速度控制回路

### Question

设计 VFL/VFM 与其他执行元件的回路时，定位夹紧顺序、回油背压和流量控制分别有什么要求？

### Standard Answer

定位夹紧顺序必须先让 VFL/VFM 扩径定位销完成定位，再动作其他执行元件；顺序错误会导致精度不良或机器损坏。若油箱回油侧有背压，应使用推荐开启压力小于 0.04 MPa 的单向阀；流量必须调整到不会产生脉冲高压。

### Scoring Standard

- P1 [17]: 先动作 VFL/VFM 扩径定位销。
- P2 [17]: 后动作其他执行元件。
- P3 [16]: 顺序错误会导致定位精度不良。
- P4 [16]: 顺序错误会导致机器损坏。
- P5 [17]: 回油有背压时使用开启压力小于 0.04 MPa 的单向阀。
- P6 [17]: 调整流量以避免脉冲高压。

### Accepted Variants

- “止回阀”可等同于“单向阀”。

### Forbidden Errors

- 先夹紧再定位，或把 0.04 MPa 说成系统使用压力。

### Tolerance

- 单向阀推荐开启压力必须小于 0.04 MPa。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 43
- Printed page: 1399-1400
- Section: 参考回路范例
- Local scope path: VFL/VFM > 参考回路 > 定位顺序、背压和流量
- Evidence type: PROCEDURE
- Evidence: VFL 与 VFM 回路注意事项均列出先定位、背压单向阀和防脉冲高压三项要求。

## VFLVFM-Q-0017

**Type: CALCULATION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: C/D 两销孔间距误差预算

### Question

PDF 要求 `C 菱形销容许偏心量 ≥ 定位销安装孔间距误差 + 工件加工孔间距误差`。若所选 C 销容许偏心量为 ±0.10 mm，实际定位销安装孔间距误差为 ±0.02 mm，工件加工孔间距误差最多可分配多少？

### Standard Answer

按最不利同向叠加：`0.10 − 0.02 = 0.08 mm`，所以工件加工孔间距误差最多为 **±0.08 mm**。回代为 `0.02 + 0.08 = 0.10 mm`，恰好不超过 C 销的容许偏心量。

### Scoring Standard

- P1 [20]: 使用容许偏心量不小于两项间距误差之和的关系。
- P2 [20]: 采用最不利同向叠加。
- P3 [20]: 正确计算 `0.10−0.02=0.08 mm`。
- P4 [20]: 最终 Gold 明确为 ±0.08 mm。
- P5 [20]: 回代核对为 `0.02+0.08=0.10 mm`。

### Accepted Variants

- 可写“单边误差预算 0.08 mm”，但必须保留 ± 公差语义。

### Forbidden Errors

- 将两项误差平方和开根号，或把可分配误差算为 ±0.12 mm。

### Tolerance

- Gold: ±0.08 mm；精确判定。

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 41
- Printed page: 1397-1398
- Section: VFL/VFM 的间距精度
- Local scope path: VFL/VFM 注意事项 > 设计 > 容许偏心量与孔间距误差
- Evidence type: FORMULA
- Evidence: 页面明确给出容许偏心量应大于等于定位销间距精度与工件加工孔间距精度之和。

## VFLVFM-Q-0018

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFL / VFM 扩径定位销
- Model / Scope: 工件孔精度与薄壁部验证

### Question

VFL/VFM 对工件定位孔的加工精度有什么最低要求？若孔周围存在薄壁部，为什么不能只按目录值直接投产，应如何处置？

### Standard Answer

工件孔加工精度应为 H8 或更好。薄壁部可能在扩径动作时发生变形，使定位精度达不到规定值，因此必须在正式使用前用实际工件进行动作测试，确认变形与定位精度可以接受后再投产。

### Scoring Standard

- P1 [25]: 工件孔加工精度要求为 H8 或更好。
- P2 [25]: 薄壁部可能在扩径时发生变形。
- P3 [25]: 变形会使定位精度达不到规定值。
- P4 [25]: 正式使用前必须用实际条件进行动作测试。

### Accepted Variants

- “H8 以上”按目录语义接受为 H8 或更高精度。

### Forbidden Errors

- 声称薄壁孔只要名义直径合格就无需验证。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 1395-1396
- Section: 工件孔周围的壁厚
- Local scope path: 扩径定位销注意事项 > 设计 > 薄壁孔
- Evidence type: CAUTION
- Evidence: 注意事项说明薄壁孔会因扩径变形影响精度，并要求正式使用前进行动作测试；型号页规定孔精度 H8 以上。

## VFLVFM-Q-0019

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: VFL-M / VFM-M 释放动作确认型
- Model / Scope: M 型排气口防护

### Question

M 释放动作确认型的排气口为什么需要特别防护？板式配管和无法做板式深孔时分别应如何处置？

### Standard Answer

排气口必须防止冷却液、切削屑和其他异物侵入，否则释放确认功能及机器正常功能会受损。板式配管时，应通过板式深孔把排气口引到不受冷却液或切削屑影响的位置；若现场受冷却液影响且不能做该深孔，应采用外部配管把排气口移到不受影响的位置。

### Scoring Standard

- P1 [20]: 排气口需防止冷却液侵入。
- P2 [20]: 排气口需防止切削屑或其他异物侵入。
- P3 [20]: 异物侵入会使释放动作确认功能异常。
- P4 [20]: 板式配管用深孔把排气口移到安全位置。
- P5 [20]: 无法做板式深孔时改用外部配管移位。

### Accepted Variants

- “泄气口”可等同于“排气口”。

### Forbidden Errors

- 将 M 型排气口封死，或让其直接暴露在冷却液区域。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 41
- Printed page: 1397-1398
- Section: 请正确处置排气口
- Local scope path: VFL/VFM 注意事项 > 安装施工 > M 型排气口
- Evidence type: CAUTION
- Evidence: 页面分别给出板式深孔与外部配管两种排气口移位方案及异物侵入后果。

## VFLVFM-Q-0020

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: VFL / VFM 适用的液压系列共通要求
- Model / Scope: VFLVFM_R00_2023KW_C1N.pdf :: 液压安装施工、操作和维护

### Question

首次施工和后续维护 VFL/VFM 液压回路时，至少应完成哪些清洁、排气、安全和定期检查工作？

### Standard Answer

配管、接头和夹具流体孔在连接前必须彻底清洗，防止异物和切削屑进入；施工后应在回路高点/末端等适当位置排气，排出含空气的液压油，并在需要处设置排气阀。操作前应清除工件和托盘上的异物，避免人员进入动作范围。维护时应定期排气，检查配管、安装螺栓、螺母、固定环等是否松动，并检查液压油是否老化，发现异常应处理后再使用。

### Scoring Standard

- P1 [10]: 配管连接前必须彻底清洗。
- P2 [10]: 管接头连接前必须彻底清洗。
- P3 [10]: 夹具流体孔连接前必须彻底清洗。
- P4 [10]: 清洗应防止异物和切削屑进入回路。
- P5 [10]: 在高点或末端等适当位置排出含空气的液压油。
- P6 [10]: 必要时设置排气阀。
- P7 [10]: 操作前清除工件和托盘上的异物。
- P8 [10]: 人员不得进入机器动作范围。
- P9 [4]: 后续维护应定期对回路排气。
- P10 [4]: 后续维护应检查配管是否松动。
- P11 [4]: 后续维护应检查安装螺栓等紧固件是否松动。
- P12 [4]: 后续维护应检查液压油是否老化。
- P13 [4]: 发现异常后必须处理完成再继续使用。

### Accepted Variants

- 紧固件检查可列出安装螺栓、螺母、固定环中的任意两个作为例子。

### Forbidden Errors

- 带压拆装、忽略排气，或在发现松动/油液老化后继续运行。

### Tolerance

- N/A

### Source

- PDF: VFLVFM_R00_2023KW_C1N.pdf
- Physical page: 45-48
- Printed page: 1725-1728
- Section: 安装施工方面的注意事项 / 操作方面的注意事项 / 保养、检查
- Local scope path: 液压系列通用 > 施工、操作与维护
- Evidence type: PROCEDURE
- Evidence: 共通页依次规定回路清洁与排气、操作安全、异物确认、定期紧固检查及液压油检查。
