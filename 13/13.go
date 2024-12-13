package main

import (
	"fmt"
	"sync"
)

func main() {

	var totalTokens int64
	results := make(chan int64, len(games))
	var wg sync.WaitGroup

	for idx, game := range games {
		wg.Add(1)
		go func(idx int, game [][]int64) {
			defer wg.Done()
			l1 := game[0]
			l2 := game[1]
			l3 := game[2]

			var possibleSolutions []int64
			a := int64(0)

			for {

				asumX := l1[0] * a
				asumY := l1[1] * a

				restX := l3[0] - asumX
				restY := l3[1] - asumY

				if a%100000000 == 0 {
					fmt.Println(idx, a, restX, restY)
				}
				if restX < 0 || restY < 0 {
					break
				}

				if l2[0] == 0 || l2[1] == 0 {
					a++
					continue
				}

				if restX%l2[0] == 0 && restY%l2[1] == 0 && restX/l2[0] == restY/l2[1] {
					x := restX / l2[0]
					if x < 0 {
						a++
						continue
					}
					possibleSolutions = append(possibleSolutions, x+a*3)
					break
				}
				a++
			}

			if len(possibleSolutions) >= 1 {
				results <- minInt64(possibleSolutions)
			}
		}(idx, game)
	}

	wg.Wait()
	close(results)

	for tokens := range results {
		totalTokens += tokens
	}

	fmt.Println(totalTokens)
}

func minInt64(slice []int64) int64 {
	min := slice[0]
	for _, v := range slice {
		if v < min {
			min = v
		}
	}
	return min
}

var games = [][][]int64{
	{
		{16, 32},
		{53, 11},
		{10000000006788, 10000000004716},
	},
	{
		{12, 23},
		{58, 33},
		{10000000017048, 10000000003330},
	},
	{
		{11, 85},
		{79, 25},
		{10000000001025, 10000000000895},
	},
	{
		{98, 41},
		{59, 88},
		{10000000006029, 10000000006258},
	},
	{
		{31, 88},
		{75, 36},
		{10000000008434, 10000000008728},
	},
	{
		{68, 17},
		{14, 76},
		{10000000005034, 10000000002051},
	},
	{
		{19, 79},
		{61, 11},
		{10000000005836, 10000000006796},
	},
	{
		{17, 90},
		{34, 11},
		{10000000001496, 10000000005047},
	},
	{
		{74, 27},
		{45, 57},
		{10000000007128, 10000000004224},
	},
	{
		{38, 17},
		{46, 71},
		{10000000015880, 10000000017830},
	},
	{
		{90, 70},
		{28, 95},
		{10000000007624, 10000000007980},
	},
	{
		{12, 35},
		{59, 35},
		{10000000004954, 10000000013535},
	},
	{
		{69, 35},
		{12, 35},
		{10000000006164, 10000000018540},
	},
	{
		{37, 91},
		{59, 12},
		{10000000002593, 10000000003449},
	},
	{
		{30, 17},
		{32, 55},
		{10000000016556, 10000000007983},
	},
	{
		{52, 99},
		{47, 15},
		{10000000008241, 10000000008316},
	},
	{
		{85, 24},
		{80, 96},
		{10000000008970, 10000000003120},
	},
	{
		{11, 62},
		{78, 31},
		{10000000014969, 10000000002068},
	},
	{
		{11, 44},
		{69, 16},
		{10000000017891, 10000000008804},
	},
	{
		{85, 32},
		{80, 99},
		{10000000006230, 10000000003172},
	},
	{
		{36, 58},
		{41, 12},
		{10000000015762, 10000000012242},
	},
	{
		{75, 37},
		{15, 52},
		{10000000016820, 10000000010024},
	},
	{
		{18, 40},
		{64, 45},
		{10000000014436, 10000000003330},
	},
	{
		{80, 39},
		{18, 57},
		{10000000009792, 10000000004718},
	},
	{
		{61, 32},
		{33, 64},
		{10000000013380, 10000000014880},
	},
	{
		{34, 14},
		{12, 30},
		{10000000009922, 10000000005550},
	},
	{
		{50, 11},
		{41, 85},
		{10000000005724, 10000000012433},
	},
	{
		{12, 28},
		{65, 23},
		{10000000014265, 10000000012207},
	},
	{
		{18, 40},
		{43, 28},
		{10000000003912, 10000000014880},
	},
	{
		{34, 35},
		{12, 96},
		{10000000003226, 10000000007085},
	},
	{
		{13, 93},
		{46, 26},
		{10000000001719, 10000000006539},
	},
	{
		{17, 34},
		{95, 55},
		{10000000005475, 10000000004740},
	},
	{
		{50, 14},
		{12, 29},
		{10000000010234, 10000000001781},
	},
	{
		{49, 13},
		{13, 23},
		{10000000013698, 10000000014190},
	},
	{
		{11, 46},
		{70, 17},
		{10000000002881, 10000000003776},
	},
	{
		{23, 56},
		{39, 12},
		{10000000006533, 10000000004688},
	},
	{
		{59, 35},
		{16, 48},
		{10000000016345, 10000000009777},
	},
	{
		{25, 97},
		{75, 18},
		{10000000003550, 10000000003127},
	},
	{
		{98, 44},
		{51, 74},
		{10000000007348, 10000000005752},
	},
	{
		{17, 65},
		{80, 26},
		{10000000004858, 10000000006412},
	},
	{
		{57, 15},
		{53, 69},
		{10000000005107, 10000000005583},
	},
	{
		{44, 25},
		{24, 42},
		{10000000004088, 10000000002306},
	},
	{
		{15, 89},
		{83, 33},
		{10000000004908, 10000000005688},
	},
	{
		{11, 40},
		{56, 36},
		{10000000018170, 10000000017932},
	},
	{
		{58, 49},
		{32, 90},
		{10000000003938, 10000000006853},
	},
	{
		{72, 23},
		{11, 44},
		{10000000017579, 10000000015676},
	},
	{
		{76, 20},
		{48, 81},
		{10000000005692, 10000000006899},
	},
	{
		{65, 22},
		{22, 51},
		{10000000008056, 10000000002070},
	},
	{
		{27, 17},
		{20, 89},
		{10000000003108, 10000000007229},
	},
	{
		{73, 22},
		{16, 52},
		{10000000013532, 10000000007976},
	},
	{
		{56, 43},
		{11, 46},
		{10000000005310, 10000000005955},
	},
	{
		{31, 17},
		{26, 55},
		{10000000004521, 10000000016495},
	},
	{
		{57, 39},
		{46, 99},
		{10000000003391, 10000000007047},
	},
	{
		{44, 93},
		{82, 23},
		{10000000005692, 10000000003613},
	},
	{
		{93, 17},
		{40, 67},
		{10000000003655, 10000000001265},
	},
	{
		{73, 44},
		{11, 37},
		{10000000000535, 10000000004518},
	},
	{
		{98, 56},
		{37, 66},
		{10000000004967, 10000000003870},
	},
	{
		{44, 16},
		{36, 63},
		{10000000008912, 10000000002489},
	},
	{
		{44, 20},
		{37, 59},
		{10000000004830, 10000000004322},
	},
	{
		{44, 11},
		{17, 78},
		{10000000006360, 10000000016470},
	},
	{
		{17, 64},
		{59, 48},
		{10000000004190, 10000000006720},
	},
	{
		{20, 56},
		{68, 12},
		{10000000006744, 10000000002292},
	},
	{
		{19, 53},
		{37, 20},
		{10000000009527, 10000000000602},
	},
	{
		{12, 71},
		{82, 16},
		{10000000004452, 10000000016281},
	},
	{
		{33, 59},
		{46, 24},
		{10000000016958, 10000000019630},
	},
	{
		{64, 14},
		{26, 69},
		{10000000019736, 10000000001322},
	},
	{
		{46, 22},
		{16, 54},
		{10000000001600, 10000000018804},
	},
	{
		{17, 68},
		{54, 24},
		{10000000004629, 10000000006228},
	},
	{
		{54, 15},
		{15, 74},
		{10000000013550, 10000000009934},
	},
	{
		{73, 12},
		{38, 48},
		{10000000008303, 10000000002868},
	},
	{
		{24, 14},
		{25, 47},
		{10000000017489, 10000000001087},
	},
	{
		{14, 45},
		{51, 18},
		{10000000006536, 10000000001808},
	},
	{
		{63, 30},
		{17, 58},
		{10000000004172, 10000000006824},
	},
	{
		{44, 19},
		{15, 31},
		{10000000017131, 10000000001327},
	},
	{
		{38, 12},
		{23, 55},
		{10000000003692, 10000000002598},
	},
	{
		{26, 53},
		{36, 22},
		{10000000004840, 10000000007052},
	},
	{
		{36, 55},
		{63, 12},
		{10000000002988, 10000000004228},
	},
	{
		{71, 30},
		{20, 59},
		{10000000001561, 10000000016507},
	},
	{
		{42, 15},
		{17, 34},
		{10000000002543, 10000000012806},
	},
	{
		{72, 48},
		{20, 57},
		{10000000003380, 10000000006489},
	},
	{
		{19, 44},
		{71, 47},
		{10000000010116, 10000000003015},
	},
	{
		{68, 16},
		{22, 71},
		{10000000005228, 10000000002020},
	},
	{
		{34, 12},
		{23, 59},
		{10000000002871, 10000000001583},
	},
	{
		{20, 53},
		{34, 12},
		{10000000011966, 10000000007093},
	},
	{
		{11, 31},
		{50, 12},
		{10000000015300, 10000000014926},
	},
	{
		{24, 48},
		{62, 39},
		{10000000014476, 10000000016502},
	},
	{
		{15, 57},
		{20, 12},
		{10000000000925, 10000000001275},
	},
	{
		{71, 34},
		{14, 54},
		{10000000017647, 10000000015614},
	},
	{
		{50, 15},
		{16, 58},
		{10000000003404, 10000000015682},
	},
	{
		{23, 59},
		{70, 34},
		{10000000001845, 10000000011637},
	},
	{
		{39, 13},
		{14, 44},
		{10000000003710, 10000000019734},
	},
	{
		{28, 48},
		{32, 15},
		{10000000003284, 10000000009737},
	},
	{
		{87, 17},
		{28, 54},
		{10000000008764, 10000000004236},
	},
	{
		{23, 12},
		{11, 50},
		{10000000012590, 10000000003064},
	},
	{
		{46, 50},
		{82, 11},
		{10000000009718, 10000000004547},
	},
	{
		{52, 25},
		{19, 55},
		{10000000003670, 10000000016450},
	},
	{
		{50, 29},
		{24, 47},
		{10000000019334, 10000000004480},
	},
	{
		{29, 12},
		{34, 67},
		{10000000017630, 10000000019800},
	},
	{
		{20, 45},
		{48, 23},
		{10000000013688, 10000000013663},
	},
	{
		{42, 84},
		{75, 35},
		{10000000007386, 10000000007182},
	},
	{
		{28, 57},
		{33, 18},
		{10000000016486, 10000000009383},
	},
	{
		{16, 56},
		{79, 40},
		{10000000012085, 10000000004488},
	},
	{
		{32, 11},
		{30, 43},
		{10000000011076, 10000000003623},
	},
	{
		{43, 45},
		{69, 17},
		{10000000004224, 10000000001660},
	},
	{
		{31, 13},
		{44, 71},
		{10000000005441, 10000000002804},
	},
	{
		{95, 33},
		{20, 42},
		{10000000006340, 10000000004656},
	},
	{
		{15, 50},
		{66, 17},
		{10000000013103, 10000000006656},
	},
	{
		{55, 28},
		{38, 64},
		{10000000006727, 10000000012972},
	},
	{
		{44, 11},
		{14, 27},
		{10000000009660, 10000000000483},
	},
	{
		{19, 79},
		{82, 37},
		{10000000005154, 10000000008664},
	},
	{
		{40, 98},
		{60, 25},
		{10000000003740, 10000000005625},
	},
	{
		{45, 11},
		{17, 78},
		{10000000017054, 10000000007039},
	},
	{
		{60, 19},
		{13, 27},
		{10000000012610, 10000000004381},
	},
	{
		{27, 53},
		{50, 31},
		{10000000007285, 10000000005523},
	},
	{
		{83, 25},
		{29, 98},
		{10000000009774, 10000000009014},
	},
	{
		{15, 67},
		{75, 19},
		{10000000012275, 10000000002439},
	},
	{
		{27, 66},
		{53, 29},
		{10000000004020, 10000000004095},
	},
	{
		{67, 34},
		{19, 52},
		{10000000002642, 10000000012674},
	},
	{
		{39, 11},
		{12, 67},
		{10000000012602, 10000000007573},
	},
	{
		{48, 80},
		{98, 38},
		{10000000010176, 10000000004928},
	},
	{
		{86, 63},
		{18, 87},
		{10000000004980, 10000000006084},
	},
	{
		{47, 12},
		{38, 72},
		{10000000017665, 10000000014996},
	},
	{
		{38, 70},
		{50, 24},
		{10000000017126, 10000000011366},
	},
	{
		{26, 49},
		{46, 21},
		{10000000008006, 10000000003833},
	},
	{
		{13, 59},
		{84, 35},
		{10000000005229, 10000000014982},
	},
	{
		{14, 84},
		{83, 15},
		{10000000000767, 10000000012359},
	},
	{
		{52, 15},
		{23, 51},
		{10000000002423, 10000000004130},
	},
	{
		{80, 86},
		{18, 94},
		{10000000004434, 10000000007230},
	},
	{
		{46, 13},
		{13, 45},
		{10000000015345, 10000000012288},
	},
	{
		{54, 17},
		{21, 65},
		{10000000012962, 10000000007239},
	},
	{
		{38, 12},
		{36, 70},
		{10000000019066, 10000000013236},
	},
	{
		{67, 97},
		{42, 16},
		{10000000006900, 10000000007346},
	},
	{
		{48, 17},
		{28, 66},
		{10000000012428, 10000000006779},
	},
	{
		{51, 22},
		{29, 61},
		{10000000002681, 10000000003727},
	},
	{
		{78, 67},
		{16, 65},
		{10000000006426, 10000000007365},
	},
	{
		{39, 60},
		{48, 21},
		{10000000014303, 10000000013676},
	},
	{
		{48, 23},
		{27, 50},
		{10000000003065, 10000000015585},
	},
	{
		{72, 41},
		{48, 94},
		{10000000007608, 10000000005799},
	},
	{
		{53, 82},
		{33, 12},
		{10000000007943, 10000000012152},
	},
	{
		{58, 31},
		{25, 56},
		{10000000000978, 10000000012450},
	},
	{
		{28, 54},
		{31, 16},
		{10000000009052, 10000000001182},
	},
	{
		{19, 25},
		{78, 16},
		{10000000006042, 10000000003012},
	},
	{
		{68, 22},
		{11, 70},
		{10000000006952, 10000000005124},
	},
	{
		{36, 12},
		{41, 77},
		{10000000017252, 10000000003044},
	},
	{
		{56, 87},
		{71, 18},
		{10000000012218, 10000000010305},
	},
	{
		{73, 88},
		{61, 20},
		{10000000007058, 10000000008080},
	},
	{
		{99, 63},
		{16, 49},
		{10000000009732, 10000000007707},
	},
	{
		{34, 71},
		{41, 26},
		{10000000003912, 10000000005546},
	},
	{
		{75, 11},
		{29, 57},
		{10000000004779, 10000000003391},
	},
	{
		{16, 36},
		{41, 29},
		{10000000002328, 10000000006884},
	},
	{
		{57, 15},
		{59, 92},
		{10000000004620, 10000000003510},
	},
	{
		{19, 72},
		{65, 61},
		{10000000002406, 10000000007079},
	},
	{
		{25, 60},
		{48, 11},
		{10000000011531, 10000000010602},
	},
	{
		{48, 12},
		{21, 52},
		{10000000012905, 10000000010256},
	},
	{
		{55, 14},
		{16, 39},
		{10000000003639, 10000000003499},
	},
	{
		{18, 69},
		{57, 13},
		{10000000001841, 10000000003718},
	},
	{
		{82, 49},
		{16, 47},
		{10000000011154, 10000000015893},
	},
	{
		{41, 12},
		{37, 69},
		{10000000008225, 10000000011330},
	},
	{
		{54, 17},
		{14, 63},
		{10000000000394, 10000000011529},
	},
	{
		{75, 26},
		{18, 58},
		{10000000007085, 10000000018528},
	},
	{
		{61, 35},
		{14, 39},
		{10000000007585, 10000000013612},
	},
	{
		{30, 67},
		{47, 13},
		{10000000015083, 10000000014276},
	},
	{
		{89, 11},
		{20, 16},
		{10000000003756, 10000000001560},
	},
	{
		{26, 53},
		{57, 34},
		{10000000018986, 10000000014053},
	},
	{
		{42, 66},
		{44, 20},
		{10000000002120, 10000000002960},
	},
	{
		{12, 40},
		{74, 40},
		{10000000004890, 10000000003280},
	},
	{
		{22, 12},
		{30, 56},
		{10000000014898, 10000000012424},
	},
	{
		{34, 17},
		{33, 94},
		{10000000003615, 10000000006225},
	},
	{
		{25, 28},
		{70, 12},
		{10000000001785, 10000000000472},
	},
	{
		{39, 96},
		{50, 21},
		{10000000008438, 10000000010869},
	},
	{
		{45, 97},
		{82, 56},
		{10000000011546, 10000000013054},
	},
	{
		{72, 71},
		{20, 82},
		{10000000003404, 10000000009024},
	},
	{
		{15, 62},
		{89, 29},
		{10000000002187, 10000000002940},
	},
	{
		{56, 26},
		{31, 67},
		{10000000007560, 10000000008454},
	},
	{
		{40, 20},
		{25, 61},
		{10000000006915, 10000000017515},
	},
	{
		{18, 76},
		{75, 11},
		{10000000007427, 10000000013459},
	},
	{
		{65, 41},
		{42, 91},
		{10000000007655, 10000000008699},
	},
	{
		{54, 46},
		{26, 74},
		{10000000003206, 10000000003094},
	},
	{
		{38, 40},
		{11, 78},
		{10000000003552, 10000000009584},
	},
	{
		{84, 31},
		{36, 50},
		{10000000003492, 10000000002794},
	},
	{
		{55, 24},
		{20, 63},
		{10000000005845, 10000000003641},
	},
	{
		{15, 50},
		{71, 31},
		{10000000001608, 10000000004743},
	},
	{
		{13, 51},
		{33, 13},
		{10000000002343, 10000000018073},
	},
	{
		{12, 31},
		{69, 55},
		{10000000006159, 10000000005188},
	},
	{
		{71, 25},
		{17, 66},
		{10000000015409, 10000000002325},
	},
	{
		{70, 31},
		{13, 44},
		{10000000006851, 10000000009483},
	},
	{
		{23, 16},
		{11, 30},
		{10000000012549, 10000000014808},
	},
	{
		{42, 13},
		{36, 55},
		{10000000006488, 10000000012226},
	},
	{
		{13, 63},
		{96, 23},
		{10000000001746, 10000000005808},
	},
	{
		{13, 42},
		{60, 26},
		{10000000002820, 10000000017794},
	},
	{
		{30, 47},
		{34, 16},
		{10000000010048, 10000000017922},
	},
	{
		{39, 14},
		{24, 44},
		{10000000014195, 10000000009630},
	},
	{
		{30, 74},
		{40, 12},
		{10000000013600, 10000000009780},
	},
	{
		{45, 14},
		{60, 73},
		{10000000006495, 10000000006150},
	},
	{
		{81, 40},
		{15, 92},
		{10000000003600, 10000000003808},
	},
	{
		{50, 17},
		{16, 43},
		{10000000012846, 10000000003081},
	},
	{
		{11, 56},
		{56, 11},
		{10000000015722, 10000000013787},
	},
	{
		{16, 88},
		{97, 57},
		{10000000001582, 10000000002030},
	},
	{
		{37, 81},
		{82, 11},
		{10000000002338, 10000000001074},
	},
	{
		{36, 67},
		{32, 15},
		{10000000008128, 10000000003084},
	},
	{
		{92, 33},
		{25, 95},
		{10000000007881, 10000000008419},
	},
	{
		{51, 30},
		{30, 99},
		{10000000004803, 10000000004371},
	},
	{
		{66, 15},
		{13, 58},
		{10000000005755, 10000000009922},
	},
	{
		{75, 21},
		{15, 60},
		{10000000008390, 10000000011918},
	},
	{
		{56, 25},
		{19, 48},
		{10000000007523, 10000000016722},
	},
	{
		{18, 50},
		{53, 23},
		{10000000017022, 10000000016754},
	},
	{
		{16, 35},
		{34, 20},
		{10000000016244, 10000000018770},
	},
	{
		{24, 66},
		{26, 11},
		{10000000017954, 10000000012959},
	},
	{
		{49, 16},
		{40, 77},
		{10000000017697, 10000000003668},
	},
	{
		{65, 12},
		{45, 61},
		{10000000004180, 10000000004829},
	},
	{
		{58, 23},
		{13, 65},
		{10000000019471, 10000000003477},
	},
	{
		{84, 49},
		{17, 83},
		{10000000009493, 10000000012042},
	},
	{
		{26, 67},
		{69, 26},
		{10000000003762, 10000000000247},
	},
	{
		{35, 23},
		{19, 41},
		{10000000002950, 10000000003792},
	},
	{
		{55, 26},
		{27, 76},
		{10000000001346, 10000000000826},
	},
	{
		{53, 65},
		{58, 11},
		{10000000005917, 10000000005573},
	},
	{
		{95, 15},
		{36, 99},
		{10000000009206, 10000000008079},
	},
	{
		{80, 40},
		{35, 67},
		{10000000004420, 10000000002804},
	},
	{
		{39, 45},
		{66, 14},
		{10000000005136, 10000000003440},
	},
	{
		{81, 65},
		{24, 81},
		{10000000001332, 10000000001995},
	},
	{
		{92, 62},
		{22, 54},
		{10000000005740, 10000000006062},
	},
	{
		{59, 52},
		{26, 93},
		{10000000002668, 10000000004454},
	},
	{
		{57, 13},
		{24, 50},
		{10000000018335, 10000000016341},
	},
	{
		{22, 76},
		{82, 26},
		{10000000002416, 10000000003458},
	},
	{
		{30, 73},
		{19, 11},
		{10000000003561, 10000000007291},
	},
	{
		{11, 81},
		{24, 12},
		{10000000002602, 10000000007794},
	},
	{
		{51, 79},
		{95, 24},
		{10000000006873, 10000000003257},
	},
	{
		{23, 48},
		{70, 44},
		{10000000003045, 10000000019172},
	},
	{
		{19, 92},
		{86, 18},
		{10000000002339, 10000000002162},
	},
	{
		{13, 60},
		{35, 15},
		{10000000007096, 10000000016190},
	},
	{
		{51, 22},
		{12, 35},
		{10000000012254, 10000000003351},
	},
	{
		{60, 31},
		{44, 78},
		{10000000004668, 10000000006391},
	},
	{
		{17, 43},
		{42, 19},
		{10000000003734, 10000000007603},
	},
	{
		{78, 32},
		{14, 25},
		{10000000003828, 10000000002437},
	},
	{
		{44, 17},
		{37, 60},
		{10000000003131, 10000000011574},
	},
	{
		{66, 89},
		{53, 15},
		{10000000005112, 10000000005877},
	},
	{
		{15, 59},
		{75, 27},
		{10000000012545, 10000000006573},
	},
	{
		{54, 16},
		{25, 61},
		{10000000005353, 10000000000325},
	},
	{
		{28, 19},
		{29, 88},
		{10000000004372, 10000000008979},
	},
	{
		{59, 99},
		{64, 12},
		{10000000002829, 10000000002553},
	},
	{
		{24, 80},
		{95, 67},
		{10000000005683, 10000000005711},
	},
	{
		{13, 42},
		{44, 22},
		{10000000013586, 10000000011034},
	},
	{
		{13, 27},
		{27, 11},
		{10000000001714, 10000000019578},
	},
	{
		{78, 40},
		{15, 25},
		{10000000007623, 10000000004965},
	},
	{
		{13, 38},
		{34, 19},
		{10000000013897, 10000000019462},
	},
	{
		{16, 86},
		{90, 97},
		{10000000007454, 10000000011059},
	},
	{
		{16, 74},
		{48, 14},
		{10000000000672, 10000000015348},
	},
	{
		{19, 56},
		{92, 49},
		{10000000003224, 10000000004837},
	},
	{
		{65, 11},
		{24, 84},
		{10000000019354, 10000000016330},
	},
	{
		{62, 14},
		{18, 55},
		{10000000009152, 10000000014331},
	},
	{
		{45, 89},
		{46, 14},
		{10000000006885, 10000000006689},
	},
	{
		{53, 21},
		{28, 67},
		{10000000007769, 10000000009179},
	},
	{
		{57, 83},
		{69, 18},
		{10000000010614, 10000000009105},
	},
	{
		{47, 14},
		{13, 37},
		{10000000006583, 10000000004633},
	},
	{
		{11, 59},
		{39, 15},
		{10000000011414, 10000000003470},
	},
	{
		{30, 11},
		{19, 65},
		{10000000002311, 10000000016664},
	},
	{
		{38, 21},
		{35, 61},
		{10000000018354, 10000000004375},
	},
	{
		{28, 57},
		{54, 19},
		{10000000016000, 10000000012527},
	},
	{
		{46, 21},
		{11, 56},
		{10000000003961, 10000000003371},
	},
	{
		{21, 69},
		{99, 57},
		{10000000001212, 10000000001836},
	},
	{
		{17, 71},
		{50, 11},
		{10000000005903, 10000000010901},
	},
	{
		{18, 36},
		{47, 23},
		{10000000003326, 10000000014216},
	},
	{
		{40, 99},
		{60, 45},
		{10000000007360, 10000000009936},
	},
	{
		{13, 50},
		{17, 11},
		{10000000002723, 10000000005089},
	},
	{
		{18, 61},
		{84, 14},
		{10000000008412, 10000000004418},
	},
	{
		{26, 13},
		{16, 31},
		{10000000007920, 10000000004033},
	},
	{
		{78, 32},
		{13, 48},
		{10000000007956, 10000000006592},
	},
	{
		{64, 19},
		{15, 45},
		{10000000015736, 10000000014716},
	},
	{
		{84, 36},
		{11, 49},
		{10000000009518, 10000000019202},
	},
	{
		{19, 50},
		{53, 21},
		{10000000011936, 10000000005601},
	},
	{
		{78, 13},
		{12, 49},
		{10000000008930, 10000000005295},
	},
	{
		{15, 37},
		{78, 57},
		{10000000004097, 10000000017153},
	},
	{
		{67, 25},
		{51, 85},
		{10000000006603, 10000000004245},
	},
	{
		{93, 21},
		{59, 89},
		{10000000009830, 10000000006836},
	},
	{
		{44, 17},
		{16, 41},
		{10000000001928, 10000000002068},
	},
	{
		{43, 90},
		{66, 45},
		{10000000008152, 10000000010170},
	},
	{
		{14, 41},
		{99, 34},
		{10000000007975, 10000000003137},
	},
	{
		{65, 24},
		{28, 62},
		{10000000013424, 10000000014226},
	},
	{
		{67, 12},
		{17, 74},
		{10000000007807, 10000000002320},
	},
	{
		{50, 80},
		{83, 14},
		{10000000008199, 10000000006822},
	},
	{
		{78, 92},
		{15, 86},
		{10000000007422, 10000000014492},
	},
	{
		{23, 56},
		{64, 31},
		{10000000016640, 10000000009512},
	},
	{
		{20, 99},
		{36, 15},
		{10000000002828, 10000000006981},
	},
	{
		{65, 33},
		{18, 42},
		{10000000014469, 10000000011309},
	},
	{
		{54, 74},
		{87, 14},
		{10000000010155, 10000000005814},
	},
	{
		{49, 25},
		{30, 64},
		{10000000002549, 10000000001587},
	},
	{
		{65, 41},
		{17, 33},
		{10000000000529, 10000000006313},
	},
	{
		{28, 96},
		{94, 61},
		{10000000002878, 10000000004903},
	},
	{
		{85, 12},
		{11, 78},
		{10000000012753, 10000000017192},
	},
	{
		{41, 26},
		{28, 81},
		{10000000005978, 10000000008218},
	},
	{
		{33, 14},
		{11, 47},
		{10000000005732, 10000000003748},
	},
	{
		{79, 68},
		{12, 52},
		{10000000001307, 10000000004292},
	},
	{
		{12, 40},
		{77, 49},
		{10000000001685, 10000000009105},
	},
	{
		{13, 41},
		{83, 56},
		{10000000018196, 10000000006822},
	},
	{
		{13, 46},
		{57, 17},
		{10000000000598, 10000000004502},
	},
	{
		{45, 20},
		{11, 42},
		{10000000003832, 10000000000204},
	},
	{
		{11, 37},
		{63, 26},
		{10000000005093, 10000000002816},
	},
	{
		{73, 15},
		{26, 37},
		{10000000002871, 10000000001508},
	},
	{
		{24, 87},
		{69, 23},
		{10000000003441, 10000000005887},
	},
	{
		{13, 56},
		{59, 19},
		{10000000019054, 10000000011310},
	},
	{
		{51, 27},
		{33, 71},
		{10000000005841, 10000000006197},
	},
	{
		{51, 81},
		{59, 18},
		{10000000008661, 10000000008532},
	},
	{
		{20, 96},
		{42, 33},
		{10000000004498, 10000000006585},
	},
	{
		{50, 82},
		{97, 34},
		{10000000006745, 10000000006684},
	},
	{
		{69, 25},
		{14, 48},
		{10000000011428, 10000000014726},
	},
	{
		{90, 44},
		{37, 88},
		{10000000003393, 10000000002288},
	},
	{
		{31, 74},
		{56, 17},
		{10000000002670, 10000000004040},
	},
	{
		{54, 87},
		{78, 32},
		{10000000005466, 10000000005809},
	},
	{
		{72, 26},
		{12, 67},
		{10000000001604, 10000000005033},
	},
	{
		{88, 20},
		{23, 97},
		{10000000001753, 10000000001775},
	},
	{
		{73, 27},
		{20, 57},
		{10000000011138, 10000000012104},
	},
	{
		{18, 65},
		{50, 24},
		{10000000005672, 10000000005766},
	},
	{
		{16, 55},
		{54, 20},
		{10000000018756, 10000000014580},
	},
	{
		{46, 29},
		{17, 46},
		{10000000002394, 10000000017395},
	},
	{
		{16, 60},
		{85, 49},
		{10000000007894, 10000000008562},
	},
	{
		{53, 17},
		{27, 70},
		{10000000013517, 10000000012629},
	},
	{
		{20, 73},
		{56, 16},
		{10000000008496, 10000000004948},
	},
	{
		{51, 93},
		{60, 18},
		{10000000006126, 10000000008520},
	},
	{
		{15, 43},
		{64, 38},
		{10000000005574, 10000000004926},
	},
	{
		{21, 60},
		{57, 17},
		{10000000004337, 10000000011300},
	},
}
