from random import random, randint

from matplotlib.pyplot import plot, show

untuned_variables = [0.2, 291.667, 1458.333374]

# fmt: off
recorded_times = [0.0, 0.008333206176757812, 0.016666412353515625, 0.024999618530273438, 0.033333778381347656, 0.04166698455810547, 0.05000019073486328, 0.058333396911621094, 0.0666666030883789, 0.07499980926513672, 0.08333301544189453, 0.09166622161865234, 0.10000038146972656, 0.10833358764648438, 0.11666679382324219, 0.125, 0.1333332061767578, 0.14166641235351562, 0.14999961853027344, 0.15833377838134766, 0.16666698455810547, 0.17500019073486328, 0.1833333969116211, 0.1916666030883789, 0.19999980926513672, 0.20833301544189453, 0.21666622161865234, 0.22500038146972656, 0.23333358764648438, 0.2416667938232422, 0.25, 0.2583332061767578, 0.2666664123535156, 0.27499961853027344, 0.28333377838134766, 0.29166698455810547, 0.3000001907348633, 0.3083333969116211, 0.3166666030883789, 0.3249998092651367, 0.33333301544189453, 0.34166622161865234, 0.35000038146972656, 0.3583335876464844, 0.3666667938232422, 0.375, 0.3833332061767578, 0.3916664123535156, 0.39999961853027344, 0.40833377838134766, 0.41666698455810547, 0.4250001907348633, 0.4333333969116211, 0.4416666030883789, 0.4499998092651367, 0.45833301544189453, 0.46666622161865234, 0.47500038146972656, 0.4833335876464844, 0.4916667938232422, 0.5, 0.5083332061767578, 0.5166664123535156, 0.5249996185302734, 0.5333337783813477, 0.5416669845581055, 0.5500001907348633, 0.5583333969116211, 0.5666666030883789, 0.5749998092651367, 0.5833330154418945, 0.5916662216186523, 0.6000003814697266, 0.6083335876464844, 0.6166667938232422, 0.625, 0.6333332061767578, 0.6416664123535156, 0.6499996185302734, 0.6583337783813477, 0.6666669845581055, 0.6750001907348633, 0.6833333969116211, 0.6916666030883789, 0.6999998092651367, 0.7083330154418945, 0.7166662216186523, 0.7250003814697266, 0.7333335876464844, 0.7416667938232422, 0.75, 0.7583332061767578, 0.7666664123535156, 0.7749996185302734, 0.7833337783813477, 0.7916669845581055, 0.8000001907348633, 0.8083333969116211, 0.8166666030883789, 0.8249998092651367, 0.8333330154418945, 0.8416662216186523, 0.8500003814697266, 0.8583335876464844, 0.8666667938232422, 0.875, 0.8833332061767578, 0.8916664123535156, 0.8999996185302734, 0.9083337783813477, 0.9166669845581055, 0.9250001907348633, 0.9333333969116211, 0.9416666030883789, 0.9499998092651367, 0.9583330154418945, 0.9666662216186523, 0.9750003814697266, 0.9833335876464844, 0.9916667938232422, 1.0, 1.0083332061767578, 1.0166664123535156, 1.0249996185302734, 1.0333337783813477, 1.0416669845581055, 1.0500001907348633, 1.058333396911621, 1.066666603088379, 1.0749998092651367, 1.0833330154418945, 1.0916662216186523, 1.1000003814697266, 1.1083335876464844, 1.1166667938232422, 1.125, 1.1333332061767578, 1.1416664123535156, 1.1499996185302734, 1.1583337783813477, 1.1666669845581055, 1.1750001907348633, 1.183333396911621, 1.191666603088379, 1.1999998092651367, 1.2083330154418945, 1.2166662216186523, 1.2250003814697266, 1.2333335876464844, 1.2416667938232422, 1.25, 1.2583332061767578, 1.2666664123535156, 1.2749996185302734, 1.2833337783813477, 1.2916669845581055, 1.3000001907348633, 1.308333396911621, 1.316666603088379, 1.3249998092651367, 1.3333330154418945, 1.3416662216186523, 1.3500003814697266, 1.3583335876464844, 1.3666667938232422, 1.375, 1.3833332061767578, 1.3916664123535156, 1.3999996185302734, 1.4083337783813477, 1.4166669845581055, 1.4250001907348633, 1.433333396911621, 1.441666603088379, 1.4499998092651367, 1.4583330154418945, 1.4666662216186523, 1.4750003814697266, 1.4833335876464844, 1.4916667938232422, 1.5, 1.5083332061767578, 1.5166664123535156, 1.5249996185302734, 1.5333337783813477, 1.5416669845581055, 1.5500001907348633, 1.558333396911621, 1.566666603088379, 1.5749998092651367, 1.5833330154418945, 1.5916662216186523, 1.6000003814697266, 1.6083335876464844, 1.6166667938232422, 1.625, 1.6333332061767578, 1.6416664123535156, 1.6499996185302734, 1.6583337783813477, 1.6666669845581055, 1.6750001907348633, 1.683333396911621, 1.691666603088379, 1.6999998092651367, 1.7083330154418945, 1.7166662216186523, 1.7250003814697266, 1.7333335876464844, 1.7416667938232422, 1.75, 1.7583332061767578, 1.7666664123535156, 1.7749996185302734, 1.7833337783813477, 1.7916669845581055, 1.8000001907348633, 1.808333396911621, 1.816666603088379, 1.8249998092651367, 1.8333330154418945, 1.8416662216186523, 1.8500003814697266, 1.8583335876464844, 1.8666667938232422, 1.875, 1.8833332061767578, 1.8916664123535156, 1.8999996185302734, 1.9083337783813477, 1.9166669845581055, 1.9250001907348633, 1.933333396911621, 1.941666603088379, 1.9499998092651367, 1.9583330154418945, 1.9666662216186523, 1.9750003814697266, 1.9833335876464844, 1.9916667938232422, 2.0]
recorded_heights = [17.010000228881836, 19.479999542236328, 21.979999542236328, 24.510000228881836, 27.079999923706055, 29.67999839782715, 32.30999755859375, 34.97999954223633, 37.70000076293945, 40.47999954223633, 43.31999969482422, 46.209999084472656, 49.15999984741211, 52.15999984741211, 55.21999740600586, 58.34000015258789, 61.5099983215332, 64.73999786376953, 68.0199966430664, 71.36000061035156, 74.76000213623047, 78.20999908447266, 81.72000122070312, 85.27999877929688, 88.9000015258789, 92.47999572753906, 96.00999450683594, 99.48999786376953, 102.93000030517578, 106.31999969482422, 109.66999816894531, 112.97000122070312, 116.22999572753906, 119.43999481201172, 122.61000061035156, 125.72999572753906, 128.80999755859375, 131.83999633789062, 134.8300018310547, 137.77000427246094, 140.6699981689453, 143.52000427246094, 146.3300018310547, 149.08999633789062, 151.80999755859375, 154.47999572753906, 157.11000061035156, 159.69000244140625, 162.22999572753906, 164.72000122070312, 167.1699981689453, 169.5699920654297, 171.92999267578125, 174.239990234375, 176.50999450683594, 178.72999572753906, 180.89999389648438, 183.02999877929688, 185.11000061035156, 187.14999389648438, 189.13999938964844, 191.08999633789062, 192.989990234375, 194.84999084472656, 196.6599884033203, 198.42999267578125, 200.14999389648438, 201.8300018310547, 203.45999145507812, 205.04998779296875, 206.58999633789062, 208.08999633789062, 209.5399932861328, 210.9499969482422, 212.30999755859375, 213.62998962402344, 214.89999389648438, 216.12998962402344, 217.30999755859375, 218.4499969482422, 219.5399932861328, 220.58999633789062, 221.58999633789062, 222.54998779296875, 223.45999145507812, 224.3300018310547, 225.14999389648438, 225.9199981689453, 226.64999389648438, 227.3300018310547, 227.97000122070312, 228.55999755859375, 229.11000061035156, 229.61000061035156, 230.0699920654297, 230.47999572753906, 230.84999084472656, 231.1699981689453, 231.4499969482422, 231.67999267578125, 231.8699951171875, 232.00999450683594, 232.11000061035156, 232.1599884033203, 232.1699981689453, 232.12998962402344, 232.04998779296875, 231.9199981689453, 231.75, 231.52999877929688, 231.26998901367188, 230.95999145507812, 230.61000061035156, 230.20999145507812, 229.76998901367188, 229.27999877929688, 228.75, 228.1699981689453, 227.54998779296875, 226.87998962402344, 226.1699981689453, 225.4099884033203, 224.61000061035156, 223.75999450683594, 222.8699951171875, 221.92999267578125, 220.94000244140625, 219.9099884033203, 218.8300018310547, 217.70999145507812, 216.5399932861328, 215.3300018310547, 214.0699920654297, 212.76998901367188, 211.4199981689453, 210.02999877929688, 208.58999633789062, 207.11000061035156, 205.5800018310547, 204.00999450683594, 202.38999938964844, 200.72999572753906, 199.01998901367188, 197.26998901367188, 195.47000122070312, 193.62998962402344, 191.739990234375, 189.80999755859375, 187.8300018310547, 185.80999755859375, 183.739990234375, 181.62998962402344, 179.47000122070312, 177.26998901367188, 175.01998901367188, 172.72999572753906, 170.38999938964844, 168.00999450683594, 165.5800018310547, 163.11000061035156, 160.58999633789062, 158.02999877929688, 155.4199981689453, 152.76998901367188, 150.0699920654297, 147.3300018310547, 144.5399932861328, 141.70999145507812, 138.8300018310547, 135.91000366210938, 132.94000244140625, 129.92999267578125, 126.8699951171875, 123.7699966430664, 120.6199951171875, 117.43000030517578, 114.18999481201172, 110.90999603271484, 107.57999420166016, 104.20999908447266, 100.79000091552734, 97.32999420166016, 93.81999969482422, 90.2699966430664, 86.66999816894531, 83.02999877929688, 79.33999633789062, 75.5999984741211, 71.81999969482422, 67.98999786376953, 64.1199951171875, 60.19999694824219, 56.23999786376953, 52.22999954223633, 48.18000030517578, 44.07999801635742, 39.939998626708984, 35.75, 31.51999855041504, 27.239999771118164, 23.51999855041504, 20.350000381469727, 17.729999542236328, 15.630000114440918, 14.65999984741211, 14.309999465942383, 14.289999961853027, 14.4399995803833, 14.649999618530273, 14.869999885559082, 15.089999198913574, 15.299999237060547, 15.5, 15.6899995803833, 15.859999656677246, 16.020000457763672, 16.15999984741211, 16.279998779296875, 16.389999389648438, 16.479999542236328, 16.559999465942383, 16.6299991607666, 16.690000534057617, 16.739999771118164, 16.779998779296875, 16.81999969482422, 16.850000381469727, 16.8799991607666, 16.899999618530273, 16.920000076293945, 16.940000534057617, 16.94999885559082, 16.959999084472656, 16.969999313354492, 16.979999542236328, 16.989999771118164, 17.0, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836]
# fmt: on


def predict_jump(time: float, max_first_jump_hold, jump_impulse, jump_acc) -> float:
    acc_time = min(time, max_first_jump_hold)
    pos = jump_impulse * acc_time + 0.5 * (jump_acc - 650) * acc_time ** 2
    if time < max_first_jump_hold:
        return pos
    vel = jump_impulse + (jump_acc - 650) * acc_time
    fall_time = time - acc_time
    return pos + vel * fall_time - 0.5 * 650 * fall_time ** 2


def graph(variables):
    plot(recorded_times, recorded_heights)
    plot(
        recorded_times,
        [predict_jump(time, *untuned_variables) for time in recorded_times],
    )
    plot(recorded_times, [predict_jump(time, *variables) for time in recorded_times])
    show()


def random_sign():
    return 1 if random() > 0.5 else -1


if __name__ == "__main__":
    # Crop recorded results.
    start_height: float = recorded_heights[0]
    for i, time in enumerate(recorded_times):
        recorded_heights[i] = recorded_heights[i] - start_height
        if recorded_heights[i] < 0:
            recorded_times = recorded_times[:i]
            recorded_heights = recorded_heights[:i]
            break

    # Tune variables.
    variables = untuned_variables[:]
    deltas = [abs(var) for var in variables]
    deltas[0] = 0
    deltas[1] = 0
    # deltas[2] = 0
    apply_factor = 0.00001
    iter: int = 1
    while True:
        random_deltas = [random_sign() * deltas[i] for i in range(len(variables))]
        one = [variables[i] - random_deltas[i] for i in range(len(variables))]
        two = [variables[i] + random_deltas[i] for i in range(len(variables))]
        random_index = randint(0, len(recorded_times) - 1)
        if abs(
            predict_jump(recorded_times[random_index], *one)
            - recorded_heights[random_index]
        ) < abs(
            predict_jump(recorded_times[random_index], *two)
            - recorded_heights[random_index]
        ):
            variables = [
                variables[i] - apply_factor * random_deltas[i]
                for i in range(len(variables))
            ]
        else:
            variables = [
                variables[i] + apply_factor * random_deltas[i]
                for i in range(len(variables))
            ]
        deltas = [delta * (1 - apply_factor) for delta in deltas]
        if iter % 10000 == 0:
            print(str(iter) + ": " + str(variables))
        iter += 1
        if all([delta * apply_factor < 10 ** -13 for delta in deltas]):
            break

    # Graph new variables.
    graph(variables)
