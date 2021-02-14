from typing import List, Tuple

from tuner import Tuner

# fmt: off
recorded_times = [10.0, 10.008333206176758, 10.016666412353516, 10.024999618530273, 10.033333778381348, 10.041666984558105, 10.050000190734863, 10.058333396911621, 10.066666603088379, 10.074999809265137, 10.083333015441895, 10.091666221618652, 10.100000381469727, 10.108333587646484, 10.116666793823242, 10.125, 10.133333206176758, 10.141666412353516, 10.149999618530273, 10.158333778381348, 10.166666984558105, 10.175000190734863, 10.183333396911621, 10.191666603088379, 10.199999809265137, 10.208333015441895, 10.216666221618652, 10.225000381469727, 10.233333587646484, 10.241666793823242, 10.25, 10.258333206176758, 10.266666412353516, 10.274999618530273, 10.283333778381348, 10.291666984558105, 10.300000190734863, 10.308333396911621, 10.316666603088379, 10.324999809265137, 10.333333015441895, 10.341666221618652, 10.350000381469727, 10.358333587646484, 10.366666793823242, 10.375, 10.383333206176758, 10.391666412353516, 10.399999618530273, 10.408333778381348, 10.416666984558105, 10.425000190734863, 10.433333396911621, 10.441666603088379, 10.449999809265137, 10.458333015441895, 10.466666221618652, 10.475000381469727, 10.483333587646484, 10.491666793823242, 10.5, 10.508333206176758, 10.516666412353516, 10.524999618530273, 10.533333778381348, 10.541666984558105, 10.550000190734863, 10.558333396911621, 10.566666603088379, 10.574999809265137, 10.583333015441895, 10.591666221618652, 10.600000381469727, 10.608333587646484, 10.616666793823242, 10.625, 10.633333206176758, 10.641666412353516, 10.649999618530273, 10.658333778381348, 10.666666984558105, 10.675000190734863, 10.683333396911621, 10.691666603088379, 10.699999809265137, 10.708333015441895, 10.716666221618652, 10.725000381469727, 10.733333587646484, 10.741666793823242, 10.75, 10.758333206176758, 10.766666412353516, 10.774999618530273, 10.783333778381348, 10.791666984558105, 10.800000190734863, 10.808333396911621, 10.816666603088379, 10.824999809265137, 10.833333015441895, 10.841666221618652, 10.850000381469727, 10.858333587646484, 10.866666793823242, 10.875, 10.883333206176758, 10.891666412353516, 10.899999618530273, 10.908333778381348, 10.916666984558105, 10.925000190734863, 10.933333396911621, 10.941666603088379, 10.949999809265137, 10.958333015441895, 10.966666221618652, 10.975000381469727, 10.983333587646484, 10.991666793823242, 11.0, 11.008333206176758, 11.016666412353516, 11.024999618530273, 11.033333778381348, 11.041666984558105, 11.050000190734863, 11.058333396911621, 11.066666603088379, 11.074999809265137, 11.083333015441895, 11.091666221618652, 11.100000381469727, 11.108333587646484, 11.116666793823242, 11.125, 11.133333206176758, 11.141666412353516, 11.149999618530273, 11.158333778381348, 11.166666984558105, 11.175000190734863, 11.183333396911621, 11.191666603088379, 11.199999809265137, 11.208333015441895, 11.216666221618652, 11.225000381469727, 11.233333587646484, 11.241666793823242, 11.25, 11.258333206176758, 11.266666412353516, 11.274999618530273, 11.283333778381348, 11.291666984558105, 11.300000190734863, 11.308333396911621, 11.316666603088379, 11.324999809265137, 11.333333015441895, 11.341666221618652, 11.350000381469727, 11.358333587646484, 11.366666793823242, 11.375, 11.383333206176758, 11.391666412353516, 11.399999618530273, 11.408333778381348, 11.416666984558105, 11.425000190734863, 11.433333396911621, 11.441666603088379, 11.449999809265137, 11.458333015441895, 11.466666221618652, 11.475000381469727, 11.483333587646484, 11.491666793823242, 11.5, 11.508333206176758, 11.516666412353516, 11.524999618530273, 11.533333778381348, 11.541666984558105, 11.550000190734863, 11.558333396911621, 11.566666603088379, 11.574999809265137, 11.583333015441895, 11.591666221618652, 11.600000381469727, 11.608333587646484, 11.616666793823242, 11.625, 11.633333206176758, 11.641666412353516, 11.649999618530273, 11.658333778381348, 11.666666984558105, 11.675000190734863, 11.683333396911621, 11.691666603088379, 11.699999809265137, 11.708333015441895, 11.716666221618652, 11.725000381469727, 11.733333587646484, 11.741666793823242, 11.75, 11.758333206176758, 11.766666412353516, 11.774999618530273, 11.783333778381348, 11.791666984558105, 11.800000190734863, 11.808333396911621, 11.816666603088379, 11.824999809265137, 11.833333015441895, 11.841666221618652, 11.850000381469727, 11.858333587646484, 11.866666793823242, 11.875, 11.883333206176758, 11.891666412353516, 11.899999618530273, 11.908333778381348, 11.916666984558105, 11.925000190734863, 11.933333396911621, 11.941666603088379, 11.949999809265137, 11.958333015441895, 11.966666221618652, 11.975000381469727, 11.983333587646484, 11.991666793823242, 12.0, 12.008333206176758, 12.016666412353516, 12.024999618530273, 12.033333778381348, 12.041666984558105, 12.050000190734863, 12.058333396911621, 12.066666603088379, 12.074999809265137, 12.083333015441895, 12.091666221618652, 12.100000381469727, 12.108333587646484, 12.116666793823242, 12.125, 12.133333206176758, 12.141666412353516, 12.149999618530273, 12.158333778381348, 12.166666984558105, 12.175000190734863, 12.183333396911621, 12.191666603088379, 12.199999809265137, 12.208333015441895, 12.216666221618652, 12.225000381469727, 12.233333587646484, 12.241666793823242, 12.25, 12.258333206176758, 12.266666412353516, 12.274999618530273, 12.283333778381348, 12.291666984558105, 12.300000190734863, 12.308333396911621, 12.316666603088379, 12.324999809265137, 12.333333015441895, 12.341666221618652, 12.350000381469727, 12.358333587646484, 12.366666793823242, 12.375, 12.383333206176758, 12.391666412353516, 12.399999618530273, 12.408333778381348, 12.416666984558105, 12.425000190734863, 12.433333396911621, 12.441666603088379, 12.449999809265137, 12.458333015441895, 12.466666221618652, 12.475000381469727, 12.483333587646484, 12.491666793823242, 12.5, 12.508333206176758, 12.516666412353516, 12.524999618530273, 12.533333778381348, 12.541666984558105, 12.550000190734863, 12.558333396911621, 12.566666603088379, 12.574999809265137, 12.583333015441895, 12.591666221618652, 12.600000381469727, 12.608333587646484, 12.616666793823242, 12.625, 12.633333206176758, 12.641666412353516, 12.649999618530273, 12.658333778381348, 12.666666984558105, 12.675000190734863, 12.683333396911621, 12.691666603088379, 12.699999809265137, 12.708333015441895, 12.716666221618652, 12.725000381469727, 12.733333587646484, 12.741666793823242, 12.75, 12.758333206176758, 12.766666412353516, 12.774999618530273, 12.783333778381348, 12.791666984558105, 12.800000190734863, 12.808333396911621, 12.816666603088379, 12.824999809265137, 12.833333015441895, 12.841666221618652, 12.850000381469727, 12.858333587646484, 12.866666793823242, 12.875, 12.883333206176758, 12.891666412353516, 12.899999618530273, 12.908333778381348, 12.916666984558105, 12.925000190734863, 12.933333396911621, 12.941666603088379, 12.949999809265137, 12.958333015441895, 12.966666221618652, 12.975000381469727, 12.983333587646484, 12.991666793823242]
recorded_heights = [17.010000228881836, 19.479999542236328, 21.979999542236328, 24.510000228881836, 27.079999923706055, 29.67999839782715, 32.30999755859375, 34.97999954223633, 37.70000076293945, 40.47999954223633, 43.31999969482422, 46.209999084472656, 49.15999984741211, 52.15999984741211, 55.21999740600586, 58.34000015258789, 61.5099983215332, 64.73999786376953, 68.0199966430664, 71.36000061035156, 74.76000213623047, 78.20999908447266, 81.72000122070312, 85.18000030517578, 88.5999984741211, 94.4000015258789, 100.15999603271484, 105.8699951171875, 111.54000091552734, 117.15999603271484, 122.73999786376953, 128.27000427246094, 133.75999450683594, 139.1999969482422, 144.59999084472656, 149.9499969482422, 155.25999450683594, 160.51998901367188, 165.739990234375, 170.91000366210938, 176.0399932861328, 181.1199951171875, 186.1599884033203, 191.14999389648438, 196.08999633789062, 200.989990234375, 205.83999633789062, 210.64999389648438, 215.4099884033203, 220.12998962402344, 224.79998779296875, 229.42999267578125, 234.00999450683594, 238.54998779296875, 243.0399932861328, 247.489990234375, 251.88999938964844, 256.25, 260.55999755859375, 264.8299865722656, 269.04998779296875, 273.22998046875, 277.3599853515625, 281.4499816894531, 285.489990234375, 289.489990234375, 293.44000244140625, 297.3500061035156, 301.2099914550781, 305.0299987792969, 308.79998779296875, 312.5299987792969, 316.2099914550781, 319.8399963378906, 323.42999267578125, 326.9700012207031, 330.4700012207031, 333.91998291015625, 337.3299865722656, 340.69000244140625, 344.0099792480469, 347.2799987792969, 350.5099792480469, 353.69000244140625, 356.8299865722656, 359.91998291015625, 362.9700012207031, 365.9700012207031, 368.92999267578125, 371.8399963378906, 374.7099914550781, 377.5299987792969, 380.30999755859375, 383.03997802734375, 385.72998046875, 388.3699951171875, 390.9700012207031, 393.5199890136719, 396.0299987792969, 398.489990234375, 400.9100036621094, 403.2799987792969, 405.6099853515625, 407.8899841308594, 410.1199951171875, 412.30999755859375, 414.4499816894531, 416.54998779296875, 418.5999755859375, 420.6099853515625, 422.5699768066406, 424.489990234375, 426.3599853515625, 428.19000244140625, 429.9700012207031, 431.7099914550781, 433.3999938964844, 435.04998779296875, 436.6499938964844, 438.2099914550781, 439.7200012207031, 441.19000244140625, 442.6099853515625, 443.989990234375, 445.3199768066406, 446.6099853515625, 447.8499755859375, 449.04998779296875, 450.1999816894531, 451.30999755859375, 452.3699951171875, 453.3899841308594, 454.3599853515625, 455.2799987792969, 456.1600036621094, 456.989990234375, 457.7799987792969, 458.5199890136719, 459.2200012207031, 459.8699951171875, 460.47998046875, 461.03997802734375, 461.55999755859375, 462.0299987792969, 462.4599914550781, 462.8399963378906, 463.17999267578125, 463.4700012207031, 463.7200012207031, 463.91998291015625, 464.0799865722656, 464.19000244140625, 464.2599792480469, 464.2799987792969, 464.2599792480469, 464.19000244140625, 464.0799865722656, 463.91998291015625, 463.7200012207031, 463.4700012207031, 463.17999267578125, 462.8399963378906, 462.4599914550781, 462.0299987792969, 461.55999755859375, 461.03997802734375, 460.47998046875, 459.8699951171875, 459.2200012207031, 458.5199890136719, 457.7799987792969, 456.989990234375, 456.1499938964844, 455.2699890136719, 454.3399963378906, 453.3699951171875, 452.3499755859375, 451.28997802734375, 450.17999267578125, 449.0299987792969, 447.8299865722656, 446.5899963378906, 445.29998779296875, 443.9700012207031, 442.5899963378906, 441.16998291015625, 439.6999816894531, 438.19000244140625, 436.6300048828125, 435.0299987792969, 433.3800048828125, 431.69000244140625, 429.9499816894531, 428.16998291015625, 426.3399963378906, 424.4700012207031, 422.54998779296875, 420.5899963378906, 418.5799865722656, 416.5299987792969, 414.42999267578125, 412.28997802734375, 410.0999755859375, 407.8699951171875, 405.5899963378906, 403.2699890136719, 400.8999938964844, 398.489990234375, 396.0299987792969, 393.5299987792969, 390.97998046875, 388.3899841308594, 385.75, 383.0699768066406, 380.3399963378906, 377.5699768066406, 374.75, 371.8899841308594, 368.97998046875, 366.0299987792969, 363.0299987792969, 359.989990234375, 356.8999938964844, 353.7699890136719, 350.5899963378906, 347.3699951171875, 344.1000061035156, 340.78997802734375, 337.42999267578125, 334.0299987792969, 330.5799865722656, 327.0899963378906, 323.54998779296875, 319.9599914550781, 316.3299865722656, 312.6499938964844, 308.92999267578125, 305.1600036621094, 301.3500061035156, 297.489990234375, 293.5899963378906, 289.6399841308594, 285.6499938964844, 281.6099853515625, 277.5299987792969, 273.3999938964844, 269.22998046875, 265.0099792480469, 260.75, 256.44000244140625, 252.08999633789062, 247.6899871826172, 243.25, 238.75999450683594, 234.22999572753906, 229.64999389648438, 225.02999877929688, 220.36000061035156, 215.64999389648438, 210.88999938964844, 206.08999633789062, 201.239990234375, 196.34999084472656, 191.4099884033203, 186.42999267578125, 181.39999389648438, 176.3300018310547, 171.20999145507812, 166.0500030517578, 160.83999633789062, 155.58999633789062, 150.2899932861328, 144.9499969482422, 139.55999755859375, 134.12998962402344, 128.64999389648438, 123.12999725341797, 117.55999755859375, 111.94999694824219, 106.29000091552734, 100.58999633789062, 94.83999633789062, 89.04999542236328, 83.20999908447266, 77.33000183105469, 71.4000015258789, 65.43000030517578, 59.40999984741211, 53.349998474121094, 47.23999786376953, 41.09000015258789, 34.88999938964844, 28.639999389648438, 23.31999969482422, 18.889999389648438, 15.319999694824219, 13.639999389648438, 13.0, 12.920000076293945, 13.130000114440918, 13.4399995803833, 13.769999504089355, 14.09999942779541, 14.420000076293945, 14.729999542236328, 15.00999927520752, 15.269999504089355, 15.5, 15.710000038146973, 15.899999618530273, 16.059999465942383, 16.19999885559082, 16.31999969482422, 16.43000030517578, 16.520000457763672, 16.600000381469727, 16.670000076293945, 16.729999542236328, 16.779998779296875, 16.81999969482422, 16.850000381469727, 16.8799991607666, 16.899999618530273, 16.920000076293945, 16.940000534057617, 16.94999885559082, 16.959999084472656, 16.969999313354492, 16.979999542236328, 16.989999771118164, 17.0, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836, 17.010000228881836]
# fmt: on


def predict_double_jump(
    time: float,
    max_first_jump_hold: float,
    jump_impulse: float,
    jump_acc: float,
    double_impulse_factor: float,
) -> float:
    acc_time = min(time, max_first_jump_hold)
    pos = jump_impulse * acc_time + 0.5 * (jump_acc - 650) * acc_time ** 2
    if time < max_first_jump_hold:
        return pos
    vel = (
        jump_impulse
        + (jump_acc - 650) * acc_time
        + jump_impulse * double_impulse_factor
    )
    fall_time = time - acc_time
    return pos + vel * fall_time - 0.5 * 650 * fall_time ** 2


if __name__ == "__main__":
    # Crop recorded results.
    start_time: float = recorded_times[0]
    start_height: float = recorded_heights[0]
    for i, time in enumerate(recorded_times):
        recorded_times[i] -= start_time
        recorded_heights[i] -= start_height
        if recorded_heights[i] < 0:
            recorded_times = recorded_times[:i]
            recorded_heights = recorded_heights[:i]
            break

    # Tune variables.
    recorded: Tuple[List[float], List[float]] = (recorded_times, recorded_heights)
    variables: List[float] = [0.2, 291.667, 1346.6605414091864, 1]
    tuner: Tuner = Tuner(recorded, predict_double_jump, variables, apply_factor=0.00001)
    tuner.deltas[0] = 0  # Do not tune these variables.
    tuner.deltas[1] = 0
    tuner.deltas[2] = 0
    tuner.tune()
    tuner.graph()
