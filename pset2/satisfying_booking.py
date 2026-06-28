def sweep_bookings(R):
    '''
    Sweep sorted endpoints; between consecutive times, k is the number of
    active talks on [t_i, t_{i+1}) using half-open intervals [s, t).
    '''
    by_time = {}
    for s, t in R:
        by_time.setdefault(s, []).append(1)
        by_time.setdefault(t, []).append(-1)

    times = sorted(by_time.keys())
    active = 0
    bookings = []
    seg_start = None
    last_k = None

    for i in range(len(times) - 1):
        for delta in sorted(by_time[times[i]]):
            active += delta
        t0, t1 = times[i], times[i + 1]
        if t0 >= t1:
            continue
        if active != last_k:
            if seg_start is not None:
                bookings.append((last_k, seg_start, t0))
            seg_start = t0
            last_k = active

    if seg_start is not None:
        bookings.append((last_k, seg_start, times[-1]))

    return tuple(bookings)


def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    return sweep_bookings(R)
