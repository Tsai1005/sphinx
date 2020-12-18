Features - ANC intro
----------------------------

## Requirement: 

* Hardware - a diffitial microphone need to be connected to the EVK, 
- the Positive signal wired to PA1
- the Negetive signal wired to PA2

 depend on the `board_xxx_cfg.h`

```C
/*
 *LADC_CH_MIC_L: MIC0(PA1)
 *LADC_CH_MIC_R: MIC1(PB8)
 */
#define TCFG_AUDIO_ADC_MIC_CHA        LADC_CH_MIC_L
```

```C
/*配置mic的硬件接法:单端或者差分*/
#define MIC_MODE_SINGLE_END					0 //单端mic
#define MIC_MODE_DIFF_END					1 //差分mic

#if TCFG_AUDIO_ANC_ENABLE
#define TCFG_AUDIO_MIC_MODE					MIC_MODE_DIFF_END
#define TCFG_AUDIO_MIC1_MODE				MIC_MODE_SINGLE_END
#define TCFG_MIC_CAPLESS_ENABLE				DISABLE
#define TCFG_MIC1_CAPLESS_ENABLE			DISABLE
#else
#define TCFG_AUDIO_MIC_MODE					MIC_MODE_SINGLE_END
#define TCFG_AUDIO_MIC1_MODE				MIC_MODE_SINGLE_END
#define TCFG_MIC_CAPLESS_ENABLE				DISABLE
#define TCFG_MIC1_CAPLESS_ENABLE			DISABLE
#endif/*TCFG_AUDIO_ANC_ENABLE*/
```

## Settings : 

First, it need to be config the ANC in the `board_xxx_cfg.h`

```C
/*
 *ANC配置
 */
#define ANC_CLOSE_MODE						0	//关闭
#define ANC_TEST_MODE						1	//测试使用
#define ANC_RUN_MODE						2	//正常使用
#define TCFG_AUDIO_ANC_ENABLE				ANC_RUN_MODE
#define TCFG_ANC_UART_DEBUG					0//ENABLE_THIS_MOUDLE
```

after the `TCFG_AUDIO_ANC_ENABLE` have been set, Some detailed config macros are in the 'audio_anc.h'

```C
#define ANC_COEFF_SAVE_ENABLE	1	/*ANC滤波器表保存使能*/
#define ANC_INFO_SAVE_ENABLE	0	/*ANC信息记忆:保存上一次关机时所处的降噪模式等等*/
#define ANC_TONE_PREEMPTION		0	/*ANC提示音打断播放(1)还是叠加播放(0)*/
#define ANC_TRANSPARENCY_ONLY	1	/*仅支持通透模式*/
#define ANC_BOX_READ_COEFF		1	/*支持通过工具读取ANC训练系数*/
#define ANC_FADE_EN				1	/*ANC淡入淡出使能*/
#define ANC_MODE_SYSVDD_EN 		0	/*ANC模式提高SYSVDD，避免某些IC电压太低导致ADC模块工作不正常*/
```

## Setup :  

* How to test the ANC module - run the 'anc_test' api in the audio_anc_demo.c
    
## Tranning : 

Our solution only support one stage tranning, the result can only be re-used to another earbuds for test.

after tranning the result will be store in the presisten memory in the `reserved Area` 

the `cpu/br30/tools/earphone/ANC/isd_config_AC897N.ini` 

```C
#ANC配置区，如果不想ANC配置因为代码大小变化而改变位置，从而失效，需要手动指定(flash末尾8K位置)
#4Mbit:0x7E000 8Mbit:0xFE000 16Mbit:0x1FE000
#加载了anc_gains.bin或者anc_coeff.bin，则表示使用文件里面的配置
#ANC增益配置保留区
#ANCIF_FILE=anc_gains.bin;
ANCIF_ADR=0xFE000;
ANCIF_LEN=0x80;
ANCIF_OPT=1;
#ANC系数配置保留区
#ANCIF1_FILE=anc_coeff.bin;
ANCIF1_ADR=0xFE080;
ANCIF1_LEN=0xF80;
ANCIF1_OPT=1;
```

## Tools : 

The PC tool can load & store the ANC coefficient from or to the earbuds.And use config_tool to generate `anc_gains.bin`.
The ANC tools are integrated together called `AC897N_config_tool`.
![image](https://github.com/Jieli-Tech/ac897_tempow/blob/master/doc/anc.png)

## Tranning Equipment

Our solution support wire (1-wired protocol ) & wireless (bluetooth protocol ) trainning for different purpose.
