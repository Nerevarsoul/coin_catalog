import { call, put, takeEvery, takeLatest } from 'redux-saga/effects'

function* fetchSerie(action) {
  try {
    const serie = yield call(Api.fetchSeries);
    yield put({type: 'SERIES_FETCH_SUCCEEDED', series: series});
  } catch(e) {
    yield put(type: 'SERIES_FETCH_FAILED', message: e.message});
  }
}

export default function* serieSaga() {
  yield all([
    fork(fetchSerie)
  ])
}

